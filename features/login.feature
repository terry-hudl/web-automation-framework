Feature: Login functionality

  Scenario Outline: Successful login to <platform> using  valid credentials
    Given I have chosen to login to the <platform> platform
    When I login with "valid" credentials
    Then I should successfully be logged in to the <platform> platform

    Examples:
      | platform      |
      | Hudl          |
      | Wyscout       |
      | Volleymetrics |
      | Wimu Cloud    |

  Scenario Outline: Unsuccessful login attempt to <platform> using invalid credentials - <scenario_name>
    Given I have chosen to login to the <platform> platform
    When I login with invalid credentials ("<type>")
    Then I should see login error message displayed
    And I should not be logged in to the <platform> platform

    Examples:
      | scenario_name        | platform      | type                |
      | Incorrect password   | Hudl          | incorrect_password  |
      | Blank password       | Hudl          | no_password         |
      | Incorrect password   | Wyscout       | incorrect_password  |
      | Blank password       | Wyscout       | no_password         |
      | Incorrect password   | Volleymetrics | incorrect_password  |
      | Blank password       | Volleymetrics | no_password         |
      | Incorrect password   | Wimu Cloud    | incorrect_password  |
      | Blank password       | Wimu Cloud    | no_password         |