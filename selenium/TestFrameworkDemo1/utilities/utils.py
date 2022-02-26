import softest as softest


class Utils(softest.TestCase):
    def list_item_text(self, list1, value):
        for stop in list1:
            print(stop.text)
            self.soft_assert(self.assertEqual, stop.text, value)
            if stop.text == value:
                print("assert pass")
            else:
                print("aasert fail")
        self.assert_all()

