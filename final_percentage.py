from final import Final


class FinalPercentage(Final):

    def __init__(self, class_name, current_grade, final_worth, goal):
        self._class_name = class_name
        self._current_grade = current_grade
        self._final_worth = final_worth
        self._goal = goal
        self._need_grade = None

    def calculate_need_grd(self):
        self._need_grade = (self._goal - (((100 - self._final_worth) / 100) * self._current_grade)) / (
                    self._final_worth / 100)


class FinalPercentageLowestDrop(FinalPercentage):

    def __init__(self, class_name, current_grade, final_worth, goal, num_tests, test_worth, test_avg, low_test):
        super().__init__(class_name, current_grade, final_worth, goal)
        self._num_tests = num_tests
        self._test_worth = test_worth
        self._test_avg = test_avg
        self._low_test = low_test
        self._need_grade = None

    def calculate_need_grd(self):
        self._need_grade = float((((self._goal / 100) - (
                    (self._num_tests * (self._test_avg / 100) - (self._low_test / 100)) * (
                        (self._test_worth / 100) / self._num_test)) - (
                                               (self._current_grade / 100) * (1 - (self._final_worth / 100)) - (
                                                   self._test_avg / 100) * (self._test_worth / 100))) / (
                                  ((self._final_worth / 100) + (self._test_worth / self._num_tests) / 100)))) * 100
