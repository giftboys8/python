# Created by Edwin at 2016/12/27
Feature: Calc Fib
  In order to introduce Behave
  We Calc fib as example

  Scenario: Calc fib number
    Given we have the number <number>
    when we calc the fib
    then we get the fib number <fib_number>

    Examples:some Numbers
    | number | fib_number |
    | 1       | 1           |
    | 2       | 2           |
    | 10      | 55          |