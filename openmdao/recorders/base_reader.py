from abc import ABCMeta, abstractmethod, abstractproperty


class Case(object):
    """ Case wraps the data from a single iteration/case of a recording
    to make it more easily accessible to the user.
    """

    def __init__(self, filename, case_id, case_dict, derivs_dict=None):
        self._filename = filename
        self.case_id = case_id

        self.timestamp = case_dict.get('timestamp', None)
        self.success = case_dict.get('success', None)
        self.msg = case_dict.get('msg', None)

        self.parameters = case_dict.get('Parameters', None)
        self.unknowns = case_dict.get('Unknowns', None)
        self.residuals = case_dict.get('Residuals', None)

        if derivs_dict is None:
            self.derivs = None
        else:
            self.derivs = derivs_dict.get('Derivatives', None)

    def __getitem__(self, item):
        if self.unknowns is None:
            raise ValueError('No unknowns are available'
                             ' in file {0}'.format(self._filename))
        return self.unknowns[item]

    def _to_json(self, filename):
        pass


class CaseReaderBase(object):

    __metaclass__ = ABCMeta

    def __init__(self):
        self._filename = None

    # @abstractmethod
    # def __getitem__(self, item):
    #     pass

    @abstractmethod
    def get_case(self, case_id):
        pass

    @abstractmethod
    def list_cases(self):
        pass

    @property
    def num_cases(self):
        return len(self.list_cases())
