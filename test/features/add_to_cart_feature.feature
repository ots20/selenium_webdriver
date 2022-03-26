# Created by brl423.krk at 27/02/2022
Feature: Add to cart
  As an user I should be able to add the searched item to the cart

  Scenario: Add item to cart
    When I search an item
    Then the search page displays the results

    When I add an item to the cart
    And I close the modal popup
    And I hover the cart
    Then the item is displayed in the cart

    When I click the checkout button
    Then I get redirected to the order details page
    And the item is displayed

