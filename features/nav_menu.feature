Feature: Nav Menu Login functionality

  Background:
    Given I have opened the Hudl platform

  Scenario: Hudl Login options within the Nav are present and correct
    When I open the login options within the nav menu
    Then I should have options to login to different Hudl areas

  Scenario Outline: <platform> Login options are present and correct
    When I open the login options within the nav menu
    And I initiate logging in to the <platform> platform
    Then the <platform> login form should be displayed

    Examples:
      | platform      |
      | Hudl          |
      | Wyscout       |
      | VolleyMetrics |
      | Wimu Cloud    |


