Feature: deleterecording
  In order to delete an old record
  As a user
  I want to delete an existent record

  Background: There are a registered user and an existent recording
    Given Exists a user "user" with password "password"

  Scenario: There are registered a record with all the fields
    Given Create and login by "user" width password "password"
    Then Exists a record registered by user
      | Artist | Recording | Description | Price |
      | Mike   | 12345     | Good        | 56'09 |


    Then I want to delete the recording
    And There are 0 recording