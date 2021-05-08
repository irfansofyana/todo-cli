Feature: Main Menu
  Scenario: Main Menu Content
    Given I am user with access to terminal
    And I want to use todo-cli
    When I open todo-cli app
    Then I should see an option to create a task
    Then I should see an option to see the tasks