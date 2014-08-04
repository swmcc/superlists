from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(5)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):

		# Go to the app
		self.browser.get('http://localhost:8000')

		# The title should have 'To-Do' in it
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')

		# Add an item by default

		# Type in "Finish TDD next chapter"

		# Hitting enter should force the page to update and the page should
		# list the "Finish TDD next chapter"

		# There is still a text box wating for another item

		# Type in "Remember to upload the changed to github"

		# Page updates and now both items are on the list

		# Close session and come back again and you should see both items

		# Everything is good

		self.browser.quit()

if __name__ == '__main__':
	unittest.main()

