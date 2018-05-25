 Feature: Sellrecording
  In order to add a new record
  As a user
  I want to add a new record

  Background: There is a recording user sell
    Given  Add sell recording: by "user" with password "password"

  Scenario: Register a record with an artist, a record, a description and a price
    Given Create and login by "user" width password "password"
    Then View user "user" workspace and "password"
      | artist        | recording   | description   | price         |
      | Mike          | 12345       | Good          | 56'09         |
    And there are 1 recording