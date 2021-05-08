Feature: Create ToDo
  Scenario: Create and save the task
    Given I am user with access to terminal
    And I want to use todo-cli
    And I want to create a task
    When I open todo-cli app
    Then I should see an option to create a todo task
    When I choose the option to create a todo task
    Then I moved into a new terminal interface to create the task
    Then I can create a todo task by defining the name of the task
    And I can fill the detail description of the task
    And I can set when the task is carried out
    And I can classified the task into some tags (work, study, etc)
    Then I should be given a choice to save the task
    When I choose the save option
    Then the task should be saved into database
    Then I should see the status of the task creation whether it's success of failed
