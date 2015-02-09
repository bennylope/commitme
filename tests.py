import unittest
import commitme

try:
    from unittest import mock
except ImportError:
    import mock


class Dummy:

    @commitme.save(True)
    def method_saves(self):
        pass

    @commitme.save(False)
    def method_no_save(self):
        pass

    def save(self, *args, **kwargs):
        pass


class TestCommit(unittest.TestCase):

    @mock.patch.object(Dummy, 'save')
    def test_true_commit(self, mocked_save):
        """Ensure the save method is called"""
        d = Dummy()
        d.method_saves()
        assert mocked_save.called

    @mock.patch.object(Dummy, 'save')
    def test_true_commit_override(self, mocked_save):
        """Ensure the save method is NOT called by kwarg"""
        d = Dummy()
        d.method_saves(commit=False)
        assert not mocked_save.called

    @mock.patch.object(Dummy, 'save')
    def test_false_commit(self, mocked_save):
        """Ensure the save method is NOT called"""
        d = Dummy()
        d.method_no_save()
        assert not mocked_save.called

    @mock.patch.object(Dummy, 'save')
    def test_false_commit_override(self, mocked_save):
        """Ensure the save method is called by kwarg"""
        d = Dummy()
        d.method_saves(commit=True)
        assert mocked_save.called


if __name__ == '__main__':
    unittest.main()
