Feature: Create Task Menu
  Scenario: Create and save a task
    Given I am user within main menu
    When I choose an option to create a task
    Then I can create a task by defining the name of the task
    And I can fill the detail description of the task
    And I can set when the task is carried out
    And I can map the task into some tags (work, study, etc)
    Then I should be given a choice to save the task
    When I choose the save option
    Then the task should be saved into database
    Then I should see the status of the task creation whether it's success of failed
