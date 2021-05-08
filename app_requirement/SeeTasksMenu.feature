Feature: See Tasks Menu
  Scenario: High level
    Given I am user within main menu
    When I choose an option to see the tasks
    Then I should see the tasks that should be done at the day I open the app
    And the maximum total tasks shown in the terminal is 10
    And the tasks should be shown in a form of table
    And it's first column is the ID of the task
    And it's second column is the name of the task
    And it's third column is the tags of the task
    And I also should see an option to see the detail task
    And I also should see an option to back to main menu

  Scenario: Detail view
    Given I am user within main menu
    When I choose an option to see the tasks
    And I choose an option to see the detail task
    Then I can give the ID of the task to see the detail information
    And I should see the name of the task
    And I should see the detail description of the task
    And I should see the tags of the task