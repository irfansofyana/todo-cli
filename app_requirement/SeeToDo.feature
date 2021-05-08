Feature: See ToDo
  Scenario: High level todo tasks
    Given I am user with access to terminal
    And I want to use todo-cli
    When I open todo-cli app
    Then I should see an option to see the tasks
    When I choose the option to see the tasks
    Then I moved into a new terminal interface
    Then I should see the tasks that should be done at the day I open the app
    And the maximum total tasks shown in the terminal is 10
    And the tasks should be shown in a form of table
    And it's first column is the ID of the task
    And it's second column is the name of the task
    And it's third column is the tags of the task

  Scenario: Detail view todo task
    Given I am user in the same interface where I can see high level tasks
    Then I should see an option to see the detail task
    When I choose the option to see the detail task
    Then I can give the ID of the task to see the detail information
    Then I moved into a new terminal interface
    And I should see the name of the task
    And I should see the detail description of the task
    And I should see the tags of the task