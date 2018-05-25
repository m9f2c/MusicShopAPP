Feature: deleterecording
  In order to delete an old record
  As a user
  I want to delete an existent record

  Background: There are a registered user and an existent recording
    Given Exists a user "user" with password "password"
    And Exists a record registered by user

      | Artist | Recording | Description | Price |
      | Mike   | 12345     | Good        | 56'09 |

  Scenario: There are registered a record with all the fields

    | Artist | Recording | Description | Price |
    | Mike   | 12345     | Good        | 56'09 |

    When I delete an existent record
    Then I view the details page of the deletement
    And There are 0 recordings