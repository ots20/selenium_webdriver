# Created by brl423.krk at 26/02/2022
Feature: Registration
  As a user I should be able to register using my email

  @registration
  Scenario: Registration form display
    When I click the sign-in button
    And I register my e-mail
    Then the registration form is presented

    When I fill the registration form successfully
    Then I get logged in with my name displayed in the header

    When I click the logout button
    Then the sign-in button is displayed again in the header