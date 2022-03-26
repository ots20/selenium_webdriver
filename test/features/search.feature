# Created by brl423.krk at 21/02/2022
Feature: Search
  As a user I should be able to search for an item in the search field

  Scenario: Searching and displaying results
    When I type "printed dress" in the search field
    Then five results are displayed under the search field

    When I click the search icon
    Then the search results page is displayed
    And  five items are displayed