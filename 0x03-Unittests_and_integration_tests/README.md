0. Parameterize a unit test
Familiarize yourself with the utils.access_nested_map function and understand its purpose. Play with it in the Python console to make sure you understand.

In this task you will write the first unit test for utils.access_nested_map.

Create a TestAccessNestedMap class that inherits from unittest.TestCase.

Implement the TestAccessNestedMap.test_access_nested_map method to test that the method returns what it is supposed to.

Decorate the method with @parameterized.expand to test the function for following inputs:

nested_map={"a": 1}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a", "b")
For each of these inputs, test with assertEqual that the function returns the expected result.

The body of the test method should not be longer than 2 lines.
1. Parameterize a unit test
Implement TestAccessNestedMap.test_access_nested_map_exception. Use the assertRaises context manager to test that a KeyError is raised for the following inputs (use @parameterized.expand):

nested_map={}, path=("a",)
nested_map={"a": 1}, path=("a", "b")
Also make sure that the exception message is as expected.
2. Mock HTTP calls
Familiarize yourself with the utils.get_json function.

Define the TestGetJson(unittest.TestCase) class and implement the TestGetJson.test_get_json method to test that utils.get_json returns the expected result.

We don’t want to make any actual external HTTP calls. Use unittest.mock.patch to patch requests.get. Make sure it returns a Mock object with a json method that returns test_payload which you parametrize alongside the test_url that you will pass to get_json with the following inputs:

test_url="http://example.com", test_payload={"payload": True}
test_url="http://holberton.io", test_payload={"payload": False}
Test that the mocked get method was called exactly once (per input) with test_url as argument.

Test that the output of get_json is equal to test_payload.
3. Parameterize and patch
Read about memoization and familiarize yourself with the utils.memoize decorator.

Implement the TestMemoize(unittest.TestCase) class with a test_memoize method.

Inside test_memoize, define following class

class TestClass:

    def a_method(self):
        return 42

    @memoize
    def a_property(self):
        return self.a_method()
Use unittest.mock.patch to mock a_method. Test that when calling a_property twice, the correct result is returned but a_method is only called once using assert_called_once.
4. Parameterize and patch as decorators
Familiarize yourself with the client.GithubOrgClient class.

In a new test_client.py file, declare the TestGithubOrgClient(unittest.TestCase) class and implement the test_org method.

This method should test that GithubOrgClient.org returns the correct value.

Use @patch as a decorator to make sure get_json is called once with the expected argument but make sure it is not executed.

Use @parameterized.expand as a decorator to parametrize the test with a couple of org examples to pass to GithubOrgClient, in this order:

google
abc
Of course, no external HTTP calls should be made.
.
.
.
8. Integration test: fixtures
We want to test the GithubOrgClient.public_repos method in an integration test. That means that we will only mock code that sends external requests.

Create the TestIntegrationGithubOrgClient(unittest.TestCase) class and implement the setUpClass and tearDownClass which are part of the unittest.TestCase API.

Use @parameterized_class to decorate the class and parameterize it with fixtures found in fixtures.py. The file contains the following fixtures:

org_payload, repos_payload, expected_repos, apache2_repos
The setupClass should mock requests.get to return example payloads found in the fixtures.

Use patch to start a patcher named get_patcher, and use side_effect to make sure the mock of requests.get(url).json() returns the correct fixtures for the various values of url that you anticipate to receive.

Implement the tearDownClass class method to stop the patcher.
9. Integration tests
Implement the test_public_repos method to test GithubOrgClient.public_repos.

Make sure that the method returns the expected results based on the fixtures.

Implement test_public_repos_with_license to test the public_repos with the argument license="apache-2.0" and make sure the result matches the expected value from the fixtures.
