# sublime-php-refactr

    Note: This software is under development and in alpha state.
          It also uses a foreign software to accomplish the refactoring.

* [PHP-Refactoring-Browser](https://github.com/QafooLabs/php-refactoring-browser) by QafooLabs

## Install & Basic Usage

1. Check this repository out and move it to your sublime packages directory.

2. [Download PHP-Refactoring-Browser](http://qafoolabs.github.com/php-refactoring-browser/assets/refactor.phar)

3. Open configuration and modify the correct file path for php binary and the refactoring browser. (Default.sublime-settings)

a. Open your php file.
b. Select lines you want to refactor
c. Open command menu with "Super+Shift+P" and select "Refactr: Extract method"
d. Type the new method name into the input box

## Why?

Refactoring with sublime should also be easy.

## Refactorings

### Extract Method

Extract a range of lines into a new method and call this method from the original
location.

## Roadmap

List of Refactorings supported:

* Extract Method

List of Refactorings coming soon:

* Rename Local Variable (Prototype Done)