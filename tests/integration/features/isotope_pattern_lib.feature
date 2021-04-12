Feature: isotope-pattern-lib

  Scenario Outline: Should return correct pattern when settings are default and molecular formula is provided
    Given Molecular "<formula>" as a raw string
    When The pattern computation is triggered
    Then The resulting pattern corresponds to the one in "<file>"

    Examples:
      | formula | file |
      |         |      |

  Scenario Outline: Should return correct pattern when settings are customized and molecular formula is provided
    Given Molecular "<formula>" as a raw string
    And Different settings are provided
    When The pattern computation is triggered
    Then The resulting pattern corresponds to the one in "<file>"

    Examples:
      | formula | file |
      |         |      |
