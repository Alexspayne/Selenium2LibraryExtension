# -*- coding: utf-8 -*-

import time
from selenium.common.exceptions import (
    ElementNotVisibleException, NoSuchElementException,
    StaleElementReferenceException, WebDriverException)
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger


class _keywords():
    def __init__(self):

        pass

    def wait_until_element_has_focus(self, locator, timeout=None):
        """Waits until the element identified by `locator` has focus.
        You might rather want to use `Element Focus Should Be Set`

        | *Argument* | *Description* | *Example* |
        | locator | Selenium 2 element locator | id=my_id |
        | timeout | maximum time to wait before the function throws an element not found error (default=None) | 5s |"""

        self._info("Waiting for focus on '%s'" % (locator))
        self._wait_until_no_error(timeout, self._check_element_focus_exp, True,
                                  locator, timeout)

    def wait_until_element_does_not_have_focus(self, locator, timeout=None):
        """Waits until the element identified by `locator` doesn't have focus.
        You might rather want to use `Element Focus Should Not Be Set`

        | *Argument* | *Description* | *Example* |
        | locator | Selenium 2 element locator | id=my_id |
        | timeout | maximum time to wait before the function throws an element not found error (default=None) | 5s |"""

        self._info("Waiting until '%s' does not have focus" % (locator))
        self._wait_until_no_error(timeout, self._check_element_focus_exp,
                                  False, locator, timeout)

    def wait_until_element_attribute_is(self,
                                        locator,
                                        expected,
                                        attribute='value',
                                        strip=False,
                                        timeout=None):
        """Waits until the element identified by `locator` value is exactly the
        expected value for the given attribute.

        | *Argument* | *Description* | *Example* |
        | locator | Selenium 2 element locator | id=my_id |
        | expected | expected value | My Name Is Selenium Person |
        | attribute | name of attribute to check | value |
        | strip | boolean, determines whether it should strip the value of the field before comparison | ${True} / ${False} |
        | timeout | maximum time to wait before the function throws an element not found error (default=None) | 5s |"""

        self._info("Waiting for '%s' value to be '%s'" % (locator, expected))
        self._wait_until_no_error(timeout, self._check_element_attribute_exp,
                                  False, locator, expected, attribute, strip,
                                  timeout)

    def wait_until_element_attribute_contains(self,
                                              locator,
                                              expected,
                                              attribute='value',
                                              timeout=None):
        """Waits until the element identified by `locator` contains
        the expected value for the given attribute.

        | *Argument* | *Description* | *Example* |
        | locator | Selenium 2 element locator | id=my_id |
        | expected | expected value | Selenium Person |
        | attribute | name of attribute to check | value |
        | timeout | maximum time to wait before the function throws an element not found error (default=None) | 5s |"""

        self._info("Waiting for '%s' value to contain '%s'" %
                   (locator, expected))
        self._wait_until_no_error(timeout, self._check_element_attribute_exp,
                                  True, locator, expected, attribute, False,
                                  timeout)

    def set_element_focus(self, locator):
        """Sets focus on the element identified by `locator`. Should
        be used with elements meant to have focus only, such as
        text fields. This keywords also waits for the focus to be
        active by calling the `Wait Until Element Has Focus` keyword.

        | *Argument* | *Description* | *Example* |
        | locator | Selenium 2 element locator | id=my_id |"""

        self._info("Setting focus on element '%s'" % (locator))

        element = self._element_find(locator, True, True)
        element.send_keys(Keys.NULL)

        self._wait_until_no_error(None, self._check_element_focus, True,
                                  locator)

    def clear_input_field(self, locator, method=0):
        """Clears the text field identified by `locator`

        The element.clear() method doesn't seem to work properly on
        all browsers, so this keyword was created to offer alternatives.

        The `method` argument defines the method it should use in order
        to clear the target field.

        0 = Uses the selenium method by doing element.clear \n
        1 = Sets focus on the field and presses CTRL + A, and then DELETE \n
        2 = Repeatedly presses BACKSPACE until the field is empty

        This keyword, when using a method other than '2' does not validate it
        successfully cleared the field, you should handle this verification by yourself.
        When using the method '2', it presses delete until the field's value is empty.

        | *Argument* | *Description* | *Example* |
        | locator | Selenium 2 element locator | id=my_id |
        | method | the clearing method that should be used | no example provided |"""

        element = self._element_find(locator, True, True)

        if (int(method) == 0):

            self._info("Clearing input on element '%s'" % (locator))
            element.clear()

        elif (int(method) == 1):

            self._info(
                "Clearing input on element '%s' by pressing 'CTRL + A + DELETE'"
                % (locator))
            element.send_keys(Keys.CONTROL + 'a')
            element.send_keys(Keys.DELETE)

        elif (int(method) == 2):

            self._info(
                "Clearing input on element '%s' by repeatedly pressing BACKSPACE"
                % (locator))
            while (len(element.get_attribute('value')) != 0):

                element.send_keys(Keys.BACKSPACE)

        else:
            element.clear()

    def element_text_color_should_be(self, locator, expected):
        """Verifies the element identified by `locator` has the expected
        text color (it verifies the CSS attribute color). Color should be in
        RGBA format.

        Example of rgba format: rgba(RED, GREEN, BLUE, ALPHA)

        | *Argument* | *Description* | *Example* |
        | locator | Selenium 2 element locator | id=my_id |
        | expected | expected color | rgba(0, 128, 0, 1) |"""

        self._info("Verifying element '%s' has text color '%s'" %
                   (locator, expected))
        self._check_element_css_value(locator, 'color', expected)

    def element_background_color_should_be(self, locator, expected):
        """Verifies the element identified by `locator` has the expected
        background color (it verifies the CSS attribute background-color). Color should
        be in RGBA format.

        Example of rgba format: rgba(RED, GREEN, BLUE, ALPHA)

        | *Argument* | *Description* | *Example* |
        | locator | Selenium 2 element locator | id=my_id |
        | expected | expected color | rgba(0, 128, 0, 1) |"""

        self._info("Verifying element '%s' has background color '%s'" %
                   (locator, expected))
        self._check_element_css_value(locator, 'background-color', expected)

    def element_width_should_be(self, locator, expected):
        """Verifies the element identified by `locator` has the expected
        width. Expected width should be in pixels.

        | *Argument* | *Description* | *Example* |
        | locator | Selenium 2 element locator | id=my_id |
        | expected | expected width | 800 |"""

        self._info("Verifying element '%s' width is '%s'" %
                   (locator, expected))
        self._check_element_size(locator, 'width', expected)

    def element_height_should_be(self, locator, expected):
        """Verifies the element identified by `locator` has the expected
        height. Expected height should be in pixels.

        | *Argument* | *Description* | *Example* |
        | locator | Selenium 2 element locator | id=my_id |
        | expected | expected height | 600 |"""

        self._info("Verifying element '%s' height is '%s'" %
                   (locator, expected))
        self._check_element_size(locator, 'height', expected)

    def element_value_should_be(self, locator, expected, strip=False):
        """Verifies the element identified by `locator` has the expected value.

        | *Argument* | *Description* | *Example* |
        | locator | Selenium 2 element locator | id=my_id |
        | expected | expected value | My Name Is Selenium Person |
        | strip | Boolean, determines whether it should strip the field's value before comparison or not | ${True} / ${False} |"""

        self._info("Verifying element '%s' value is '%s'" %
                   (locator, expected))

        element = self._element_find(locator, True, True)
        value = element.get_attribute('value')

        if (strip):
            value = value.strip()

        if str(value) == expected:
            return

        else:
            raise AssertionError("Element '%s' value was not '%s', it was '%s'"
                                 % (locator, expected, value))

    def element_value_should_not_be(self, locator, value, strip=False):
        """Verifies the element identified by `locator` is not the specified value.

        | *Argument* | *Description* | *Example* |
        | locator | Selenium 2 element locator | id=my_id |
        | value | value it should not be | My Name Is Selenium Person |
        | strip | Boolean, determines whether it should strip the field's value before comparison or not | ${True} / ${False} |"""

        self._info("Verifying element '%s' value is not '%s'" %
                   (locator, value))

        element = self._element_find(locator, True, True)
        elem_value = str(element.get_attribute('value'))

        if (strip):
            elem_value = elem_value.strip()

        if elem_value == value:
            raise AssertionError(
                "Value was '%s' for element '%s' while it shouldn't have" %
                (elem_value, locator))

    def element_value_should_contain(self, locator, expected):
        """Verifies the element identified by `locator` contains the expected value.

        | *Argument* | *Description* | *Example* |
        | locator | Selenium 2 element locator | id=my_id |
        | expected | expected value | Selenium Person |"""

        self._info("Verifying element '%s' value contains '%s'" %
                   (locator, expected))

        element = self._element_find(locator, True, True)
        value = str(element.get_attribute('value'))

        if expected in value:
            return

        else:
            raise AssertionError(
                "Value '%s' did not appear in element '%s'. It's value was '%s'"
                % (expected, locator, value))

    def element_value_should_not_contain(self, locator, value):
        """Verifies the element identified by `locator` does not contain the specified value.

        | *Argument* | *Description* | *Example* |
        | locator | Selenium 2 element locator | id=my_id |
        | value | value it should not contain | Selenium Person |"""

        self._info("Verifying element '%s' value does not contain '%s'" %
                   (locator, value))

        element = self._element_find(locator, True, True)
        elem_value = str(element.get_attribute('value'))

        if value in elem_value:
            raise AssertionError(
                "Value '%s' was found in element '%s' while it shouldn't have"
                % (value, locator))

    def element_focus_should_be_set(self, locator):
        """Verifies the element identified by `locator` has focus.

        | *Argument* | *Description* | *Example* |
        | locator | Selenium 2 element locator | id=my_id |"""

        self._info("Verifying element '%s' focus is set" % locator)
        self._check_element_focus(True, locator)

    def element_focus_should_not_be_set(self, locator):
        """Verifies the element identified by `locator` does not have focus.

        | *Argument* | *Description* | *Example* |
        | locator | Selenium 2 element locator | id=my_id |"""

        self._info("Verifying element '%s' focus is not set" % locator)
        self._check_element_focus(False, locator)

    def element_css_attribute_should_be(self, locator, prop, expected):
        """Verifies the element identified by `locator` has the expected
        value for the targeted `prop`.

        | *Argument* | *Description* | *Example* |
        | locator | Selenium 2 element locator | id=my_id |
        | prop | targeted css attribute | background-color |
        | expected | expected value | rgba(0, 128, 0, 1) |"""

        self._info(
            "Verifying element '%s' has css attribute '%s' with a value of '%s'"
            % (locator, prop, expected))
        self._check_element_css_value(locator, prop, expected)

    def wait_until_page_contains_elements(self, timeout, *locators):
        """This is a copy of `Wait Until Page Contains Element` but it allows
        multiple arguments in order to wait for more than one element.

        | *Argument* | *Description* | *Example* |
        | timeout | maximum time to wait, if set to ${None} it will use Selenium's default timeout | 5s |
        | *locators | Selenium 2 element locator(s) | id=MyId |"""

        self._wait_until_no_error(timeout, self._wait_for_elements, locators)

    def wait_until_page_contains_one_of_these_elements(self, timeout,
                                                       *locators):
        """Waits until at least one of the specified elements is found.

        | *Argument* | *Description* | *Example* |
        | timeout | maximum time to wait, if set to ${None} it will use Selenium's default timeout | 5s |
        | *locators | Selenium 2 element locator(s) | id=MyId |"""

        self._wait_until_no_error(timeout, self._wait_for_at_least_one_element,
                                  locators)

    def wait_until_page_does_not_contain_these_elements(self, timeout,
                                                        *locators):
        """Waits until all of the specified elements are not found on the page.

        | *Argument* | *Description* | *Example* |
        | timeout | maximum time to wait, if set to ${None} it will use Selenium's default timeout | 5s |
        | *locators | Selenium 2 element locator(s) | id=MyId |"""

        self._wait_until_no_error(timeout, self._wait_for_elements_to_go_away,
                                  locators)

    def tap_key(self, key, complementKey=None):
        """Presses the specified `key`. The `complementKey` defines the key to hold
        when pressing the specified `key`. For example, you could use ${VK_TAB} as `key` and
        use ${VK_SHIFT} as `complementKey' in order to press Shift + Tab (back tab)

        | =Argument= | =Description= | =Example= |
        | key | the key to press | ${VK_F4} |
        | complementKey | the key to hold while pressing the key passed in previous argument | ${VK_ALT} |"""

        driver = self._current_browser()

        if (complementKey is not None):
            ActionChains(driver).key_down(complementKey).send_keys(key).key_up(
                complementKey).perform()

        else:
            ActionChains(driver).send_keys(key).perform()

    def wait_until_element_is_clickable(self, locator, timeout=None):
        """Clicks the element specified by `locator` until the operation succeeds. This should be
        used with buttons that are generated in real-time and that don't have their click handling available
        immediately. This keyword avoids unclickable element exceptions.

        | =Argument= | =Description= | =Example= |
        | locator | Selenium 2 element locator(s) | id=MyId |
        | timeout | maximum time to wait, if set to ${None} it will use Selenium's default timeout | 5s |"""

        self._wait_until_no_error(timeout, self._wait_for_click_to_succeed,
                                  locator)

    def register_webdriver(self, driver, alias=None):
        '''This lets you pass in a webdriver to the class instance for the library
        so that you can keep the state of your current webdriver and use an updated
        version of the custom library.

        Otherwise you would have to start a new browser everytime you tweaked the
        class and that would slow things down.
        '''
        self._debug("Added %s WebDriver instance with session id %s \
                    to the register" % (driver.name, driver.session_id))
        return self._cache.register(driver, alias)

    def undo(self):
        """
        Simulate a CTRL+Z keypress
        """
        driver = self._current_browser()
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('z').key_up(
            Keys.CONTROL).perform()

    def redo(self):
        """
        Simulate a CTRL+Y keypress
        """
        driver = self._current_browser()
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('y').key_up(
            Keys.CONTROL).perform()

    def clear_field(self, locator):
        """
        This empties the text from a field when selenium's clear command
        proves to be insufficient.
        It carries out a series of actions:
        1. Click on the given field.
        2. Press Ctrl + A key combination. (Select All)
        3. Press Delete key.
        """
        driver = self._current_browser()
        field = self._element_find(locator, True, True)
        field.click()
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('a').key_up(
            Keys.CONTROL).send_keys(Keys.DELETE).perform()

    def send_keys(self, key, case=None):
        """
        This function is for when we need to trigger a key press agnostic
        of any particular element.
        """
        if case == 'lower':
            key = key.lower()

        ActionChains(self._current_browser()).send_keys(key).perform()

    def get_child(self, locator, xpath="/*[1]"):
        """
        Returns a webelement beneath the element found by 'locator' using the relative `xpath`.
        ARGS:
        locator - Element to use as root for the relative xpath.
        xpath - Relative xpath from root element
        RETURNS:
        WebElement - first WebElement to match on xpath
        """
        element = self._element_find(locator, True, True)
        try:
            child = element.find_element_by_xpath("." + xpath)
        except:
            raise AssertionError("No Element was found by relative XPath %s" %
                                 (xpath))

        return child

    def get_children(self, locator, xpath="/*"):
        """
        Returns a list of webelements beneath the element found by 'locator' using the relative `xpath`.
        ARGS:
        locator - Element to use as root for the relative xpath.
        xpath - Relative xpath from root element
        RETURNS:
        WebElements - list of WebElements to match on xpath
        """
        element = self._element_find(locator, True, True)
        return element.find_elements_by_xpath("." + xpath)

    def wait_for_element_to_come_and_go(self, xpath_for_element, timeout=None):
        '''
        This waits for an animation or loading element (found by xpath) to come and go.
        A Selenium WebElement object will not work.
        '''
        # Wait until it appears first, so that it doesn't resolve before it
        # even has a chance to load.
        try:
            self.wait_until_page_contains_element(xpath_for_element, timeout)
        except:
            print 'Never saw the element. The test probably lagged and missed it.'

        # If it never appears, then this will throw an error for us too.
        self.wait_until_page_does_not_contain_element(xpath_for_element,
                                                      timeout)

    def _has_focus(self, locator):
        """
        Return True if element found by 'locator' has focus.
        """
        driver = self._current_browser()
        element = self._element_find(locator, True, True)
        focus = driver.switch_to.active_element == element
        return focus

    def wait_until_box_is_changed(self, checkbox, checked=True, timeout=None):
        """This waits for the given checkbox to become checked or unchecked."""

        if not timeout:
            timeout = self._timeout_in_secs
        error = "Checkbox didn't change in %d seconds" % (timeout)

        waiting_function = self.return_bool

        if checked:
            condition_function = self.checkbox_should_be_selected
        else:
            condition_function = self.checkbox_should_not_be_selected

        waiting_args = (condition_function, checkbox)

        self._wait_until(timeout, error, waiting_function, *waiting_args)

    def element_exists(self, locator):
        """Returns True if the given element exists.
        This is useful when you want to check if an element is on
        a page without a test fail condition."""

        try:
            self.get_webelement(locator)
            return True
        except:
            return False

    def num_elements_on_page(self, locator):
        """
        This does the same thing as len(self.get_webelements(locator))
        with one exception.  It returns a 0 instead of throwing an
        exception when no elements are found.
        """
        try:
            return len(self.get_webelements(locator))
        except:
            return 0

    def return_bool(self, function, *args):
        """
        Exceptions thrown when evaluating function(*args)
        are caught and handled by returning False.
        It returns True if the function evaluates without throwing an error.
        This allows for more flexibility in using Selenium2Library keywords.
        """
        try:
            function(*args)
            return True
        except:
            return False

    def get_created(self, xpath, creator, *args):
        """Execute creator and return a new element that matches xpath.
        ARGS:
        xpath (string) - XPath that should match the new element.
        creator (method) - This is a method that will create the new element.
        *args - Additional parameters will be passed to creator.

        RETURN: (new, value)
        new - the new WebElement matched by the xpath
        value - the return value of creator(*args)"""
        old_list = []
        try:
            # Get existing elements
            old_list = self.get_webelements(xpath)
        except:
            logger.info("There were no existing matches.")

        value = BuiltIn().run_keyword(creator, *args)

        # Wait until there is a new match for the XPath
        timeout = time.time() + self._timeout_in_secs
        self.wait_until_page_contains_element(
            xpath, None, "Never found a new element matching XPath: " + xpath)
        new_list = self.get_webelements(xpath)
        new = [x for x in new_list if x not in old_list]
        return (new[0], value)

    def wait_until_element_has_class(self,
                                     locator,
                                     expected,
                                     timeout=None,
                                     error=None):
        """
        Wait until an element identified by 'locator' has the class 'expected'.
        """

        def check_class():
            element = self._element_find(locator, True, False)
            actual = element.get_attribute("class").split(" ")
            if expected in actual:
                return
            else:
                return error or "Class '%s' did not appear in %s to element '%s'. " \
                    "Its class(es) was '%s'." % (expected,
                                                 self._format_timeout(timeout),
                                                 locator, actual)

        self._wait_until_no_error(timeout, check_class)

    def wait_until_element_does_not_have_class(self,
                                               locator,
                                               expected,
                                               timeout=None,
                                               error=None):
        """
        Wait until an element identified by 'locator' has the class 'expected'.
        """

        def check_not_has_class():
            element = self._element_find(locator, True, False)
            actual = element.get_attribute("class").split(" ")
            if expected not in actual:
                return
            else:
                return error or "Class '%s' still appeared after %s in element '%s'. " \
                    "Its class(es) were '%s'." % (expected,
                                                  self._format_timeout(
                                                      timeout),
                                                  locator, actual)

        self._wait_until_no_error(timeout, check_not_has_class)

    def element_should_have_class(self, locator, expected, message=''):
        """
        Verify that element identified by 'locator' has the class 'expected'.
        """

        self._info("Verifying element '%s' has class '%s'." %
                   (locator, expected))
        element = self._element_find(locator, True, False)
        actual = element.get_attribute("class").split(" ")
        # The reason I don't use _has_class() here is because I still want to
        # include 'actual' in the error message, but I don't want to pass this
        # to or from _has_class().
        if not expected in actual:
            if not message:
                message = "Element '%s' should have had class '%s' but "\
                          "its class(es) was '%s'." % (
                              locator, expected, actual)
            raise AssertionError(message)

    def element_should_not_have_class(self, locator, expected, message=''):
        """
        Verify that element identified by 'locator' does not have the class 'expected'.
        """

        self._info("Verifying element '%s' has class '%s'." %
                   (locator, expected))
        element = self._element_find(locator, True, False)
        actual = element.get_attribute("class").split(" ")

        if expected in actual:
            if not message:
                message = "Element '%s' should not have had class '%s' but "\
                          "its class(es) was '%s'." % (
                              locator, expected, actual)
            raise AssertionError(message)

    def validate_field_is_not_editable(self, locator):
        """Checks that the field found by the given locator is not editable."""
        field = self._element_find(locator, True, True)
        original_text = field.text
        self.add_text_to_prompt_field(field, "This Text Shouldn't make it")
        BuiltIn().should_be_equal_as_strings(
            field.text, original_text,
            "The field proved to be editable, even though it was marked.")

    def _has_class(self, locator, expected):
        """
        Returns True if give element has the specified class.
        """
        # TODO make this an instance method of the WebElement class
        element = self._element_find(locator, True, False)
        actual = element.get_attribute("class").split(" ")
        if expected in actual:
            return True
        else:
            return False

    def select_from_list_by_text(self, locator, text):
        """
        Selects `text` option from the list located by `locator`.
        """
        element = self._element_find(locator, True, True)
        options = element.find_elements_by_xpath(".//option")
        option_texts = [option.text for option in options]
        option_index = option_texts.index(text)
        self.select_from_list_by_index(element, str(option_index))

    def get_webelements_return_empty_for_none(self, locator):
        """Don't want to fail if 'get_webelements' find none"""
        try:
            return self.get_webelements(locator)
        except:
            return []

    # HELPER METHODS
    def _check_element_focus_exp(self, set, locator, timeout=None):

        if set:
            element = self._element_find(locator, True, False)
            if not element:
                return "Element locator '%s' did not match any elements after %s" % (
                    locator, self._format_timeout(timeout))

            driver = self._current_browser()
            if element == driver.switch_to.active_element:
                return
            else:
                return "Element '%s' did not get focus after %s" % (
                    locator, self._format_timeout(timeout))

        else:
            element = self._element_find(locator, True, False)
            if not element:
                return "Element locator '%s' did not match any elements after %s" % (
                    locator, self._format_timeout(timeout))

            driver = self._current_browser()
            if element != driver.switch_to.active_element:
                return
            else:
                return "Element '%s' still had focus after %s while it shouldn't have" % (
                    locator, self._format_timeout(timeout))

    def _check_element_attribute_exp(self,
                                     partial,
                                     locator,
                                     expected,
                                     attribute_name='value',
                                     strip=False,
                                     timeout=None):

        if partial:
            element = self._element_find(locator, True, False)
            if not element:
                return "Element locator '%s' did not match any elements after %s" % (
                    locator, self._format_timeout(timeout))

            attribute = str(element.get_attribute(attribute_name))

            if (strip):
                attribute = attribute.strip()

            if expected in attribute:
                return
            else:
                return "Value '%s' of '%s' attribute did not appear in %s to element '%s'. It's '%s' attribute was '%s'." % (
                    expected, attribute_name, self._format_timeout(timeout),
                    locator, attribute_name, attribute)

        else:
            element = self._element_find(locator, True, False)
            if not element:
                return "Element locator '%s' did not match any elements after %s" % (
                    locator, self._format_timeout(timeout))

            attribute = element.get_attribute(attribute_name)

            if (strip):
                attribute = attribute.strip()

            if str(attribute) == expected:
                return
            else:
                return "Element '%s' attribute '%s' value was not %s after %s" % (
                    locator, attribute_name, expected,
                    self._format_timeout(timeout))

    def _check_element_focus(self, set, locator):

        if set:
            element = self._element_find(locator, True, True)
            driver = self._current_browser()
            if element == driver.switch_to.active_element:
                return
            else:
                raise AssertionError(
                    "Element '%s' did not have focus while it should have" %
                    locator)

        else:
            element = self._element_find(locator, True, True)
            driver = self._current_browser()
            if element != driver.switch_to.active_element:
                return
            else:
                raise AssertionError(
                    "Element '%s' had focus while it shouldn't have" % locator)

    def _check_element_css_value(self, locator, prop, expected):

        element = self._element_find(locator, True, True)

        value = element.value_of_css_property(prop)
        if (value != expected):
            raise AssertionError(
                "Element locator '%s' css property '%s' had a value of '%s' while it should have been '%s'"
                % (locator, prop, value, expected))

    def _check_element_size(self, locator, type, expected):

        element = self._element_find(locator, True, True)

        size = str(element.size.get(type))
        if size != expected:
            raise AssertionError(
                "The %s of element '%s' should have been '%s' but in fact it was '%s'"
                % (type, locator, expected, size))

    def _wait_for_elements(self, locators):

        for locator in locators:

            element = self._element_find(locator, True, False)
            if not element:
                return "Element '%s' couldn't be found" % locator

    def _wait_for_at_least_one_element(self, locators):

        for locator in locators:

            element = self._element_find(locator, True, False)
            if element is not None:
                return

        return "Couldn't find any of the expected elements from '%s'" % str(
            locators)

    def _wait_for_element(self, locator):
        """Simpler implementation of Wait Until Page Contains Element"""

        element = self._element_find(locator, True, False)
        if not element:
            return "Element '%s' couldn't be found" % locator

    def _wait_for_element_to_go_away(self, locator):
        """Simpler implementation of Wait Until Page Does Not Contain Element"""
        element = self._element_find(locator, True, False)
        if element is not None:
            return "Element '%s' shouldn't have been there" % locator

    def _wait_for_elements_to_go_away(self, locators):

        for locator in locators:

            element = self._element_find(locator, True, False)
            if element is not None:
                return "Element '%s' shouldn't have been there" % locator

    def _wait_for_click_to_succeed(self, locator):
        """Clicks an element until there is no error (created to avoid click errors on periodically unclickable elements"""
        element = self._element_find(locator, True, False)
        if not element:
            return "Couldn't find the element '%s', click operation failed" % locator

        element.click()

    def blur(self, locator):
        """Removes focus from element identified by `locator`."""
        element = self._element_find(locator, True, True)
        self._current_browser().execute_script("arguments[0].blur();", element)
