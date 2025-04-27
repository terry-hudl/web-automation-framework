Feature: Single Sign On Functionality

Scenario Outline: SSO works as expected when logging in to the <platform> platform and switching to <new_platform>
    Given I have chosen to login to the <platform> platform
    When I login with "valid" credentials
    Then I should successfully be logged in to the <platform> platform

    When I navigate directly to the <new_platform> home page
    Then I should successfully be logged in to the <new_platform> platform

    Examples:
      | platform      | new_platform  |
      | Hudl          | VolleyMetrics |
      | Hudl          | Wimu Cloud    |
      | Hudl          | Wyscout       |
      | VolleyMetrics | Hudl          |
      | VolleyMetrics | Wimu Cloud    |
      | VolleyMetrics | Wyscout       |
      | Wimu Cloud    | VolleyMetrics |
      | Wimu Cloud    | Hudl          |
      | Wimu Cloud    | Wyscout       |
      | Wyscout       | VolleyMetrics |
      | Wyscout       | Wimu Cloud    |
      | Wyscout       | Hudl          |