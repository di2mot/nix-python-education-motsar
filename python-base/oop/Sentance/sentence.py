"""Iterators"""

from collections import Counter


class MultipleSentencesError(Exception):
    """Custom exclusion

    The line consists of two or more sentences.
    """
    print('The line consists of two or more sentences.')


class Sentance:
    """Container class"""

    def __init__(self, sent: str):
        """Store arguments

        :param sent: str
        :self.vanil :str - source string
        :self.sent :str - clean string
        """
        self.vanil = sent
        self.sent = self._cleaner()

        # проверяем на ошибки и райзим их
        self._errore_checker()

    def _errore_checker(self):
        """Loops through error templating engines"""
        if not self._type_checker():
            raise TypeError
        if not self._closet_checker():
            raise ValueError
        if not self._one_sent_checker():
            raise MultipleSentencesError

    def _type_checker(self):
        """Tests for compliance with type str"""
        msg = False
        if isinstance(self.vanil, str):
            msg = True
        return msg

    def _closet_checker(self) -> bool:
        """Checks if the sentence ends correctly."""
        template_1 = ('.', '!', '?',)
        template_2 = ('...', '!..', '?..', '..!', '..?')

        msg = False

        if self.vanil[-3:] in template_2:
            msg = True
        elif self.vanil[-2].isalnum() and self.vanil[-1] in template_1:
            msg = True
        return msg

    def _one_sent_checker(self) -> bool:
        """Checks a string for 1 sentence..

        First, split by point using split ().
        If one sentence is up to, you get a tuple of the type: ['abcdefg', '']
        And if the length of the string with index [0] == 0 then everything is ok.
        """

        msg = False
        if len(self.vanil.split('.')[1]) == 0:
            msg = True
        return msg

    def _cleaner(self):
        """Clears all non-alphabetic characters"""
        templ = ''
        for i in self.vanil:
            if i.isalpha() or i == ' ':
                templ += i
        return templ

    def _words(self):
        """Generator protocol"""
        for i in SentenceIterator(self.sent):
            yield i

    @property
    def words(self):
        """List of words"""
        res = []
        for i in SentenceIterator(self.sent):
            res.append(i + ' ')
        return res

    @property
    def other_chars(self):
        """List of all non-alphabetic characters"""
        res = []
        for i in self.vanil:
            if not i.isalpha():
                res.append(i)
        return set(res)

    def __repr__(self):
        """Implements __repr__"""
        words_count, other_chars_count = SentenceIterator(self.sent)._counter()
        return f'Sentence(words={words_count}, other_chars={other_chars_count})'

    def __iter__(self):
        """Implements iterator"""
        return SentenceIterator(self.sent)

    def __getitem__(self, index):
        """Implements next()"""
        return SentenceIterator(self.sent).fu_for_get_item(index)


class SentenceIterator:
    """Iterator class"""

    def __init__(self, sent):
        self.sent = sent
        self._start = 0
        self._stop = 0
        self._remains = 0
        self._words_count = 0

    def get_item(self):
        """Main iterator"""
        templ = self.sent[self._start:].find(' ')
        res = ''
        if templ == -1:
            res = self.sent[self._start:]
        elif templ != -1:
            res = self.sent[self._start:templ + self._start]
        self._start += templ + 1

        if self._stop <= self.sent.count(' '):
            self._remains -= 1
            self._stop += 1
            return res
        raise StopIteration

    def _counter(self):
        """Count the symbols"""
        words_count = 0
        other_chars_count = 0

        count = Counter(self.sent)
        for i in count:
            if i.isalpha():
                words_count += count[i]
            else:
                other_chars_count += count[i]

        return words_count, other_chars_count

    def fu_for_get_item(self, index):
        """Responsible for choosing which function to call, slice or index"""
        if isinstance(index, int):
            res = self._non_slice_for_get_item(index)
        elif isinstance(index, slice):
            res = self._slice_fo_getitem(index)
        else:
            raise TypeError
        return res

    def _non_slice_for_get_item(self, index):
        """To find only indices"""
        res = ''
        for i in range(str(self.sent).count(' ')+1):
            res = self.get_item()
            if i == index:
                break
        return res

    def _slice_fo_getitem(self, index):
        """Responsible for slicing"""
        res = ''
        count = index.start
        if not index.step:
            step = index.step
        else:
            step = 1

        for i in range(str(self.sent).count(' ')+1):
            templ = self.get_item()

            if i == count and i < index.stop:

                res += templ + ' '
                count += step
            elif i == index.stop:
                break
        return res

    def __next__(self):
        return self.get_item()

    def __iter__(self):
        return self

    def __len__(self):
        return len(self.sent)


if __name__ == "__main__":

    SENT = 'съешь ещё этих мягких французских булок, да выпей чаю.'

    iter_word = Sentance(SENT)
    print(f'Test sentence: {SENT}')
    print(f"Test 1, __repr__ : {iter_word}")
    # print(f'Test 2, generator object : {iter_word._words()}')
    # next_iter = iter_word._words()
    # print(f"Test 3, next() :{next(next_iter)}")
    # print(f"Test 3, next() :{next(next_iter)}")
    print(f"Test 4, slice[1:8:2]: {Sentance(SENT)[1:8:2]}")
    print(f"Test 5, index[4]: {Sentance(SENT)[4]}")
    print('Test 6, cycle :')
    for r in iter_word:
        print(r)
    print(f'Test 7, words: {iter_word.words}')
    print(f'Test 8, non_ite: {iter_word.other_chars}')
    # print(f'Test 9, MultipleSentencesError: {Sentance("Eorre. Errore.")}')
    # print(f'Test 10, ValueError: {Sentance("Errore,")}')
    # print(f'Test 11, TypeError: {Sentance(1)}')
