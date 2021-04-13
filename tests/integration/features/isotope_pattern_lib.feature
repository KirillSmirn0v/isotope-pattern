Feature: isotope-pattern-lib

  Scenario Outline: Should return correct pattern when settings are default and molecular formula is provided
    Given Molecular "<formula>" as a raw string
    And The pattern computation is triggered
    Then The resulting pattern corresponds to the one in "<file>"

    Examples:
      | formula    | file            |
      | CO2        | CO2.yaml        |
      | C2H5OH     | C2H5OH.yaml     |
      | CH3CH2OH   | CH3CH2OH.yaml   |
      | H2NCH2COOH | H2NCH2COOH.yaml |

  Scenario Outline: Should return correct pattern when settings are customized and molecular formula is provided
    Given Molecular "<formula>" as a raw string
    And Different settings are provided
    And The pattern computation is triggered
    Then The resulting pattern corresponds to the one in "<file>"

    Examples:
      | formula    | file            |
      | CO2        | CO2.yaml        |
      | C2H5OH     | C2H5OH.yaml     |
      | CH3CH2OH   | CH3CH2OH.yaml   |
      | H2SO4      | H2SO4.yaml      |
