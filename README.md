testify
=======

A Sublime Text plugin aimed at making writing PHPSpec specs a walk in the park.

## Installation
1. Download the file
2. Unarchive the file in Sublime Text [packages folder](http://sublimetext.info/docs/en/extensibility/packages.html)

The new menus and command palette options should appear in your Sublime Text installation.

## Usage
The plugin allows writing specs into a spec in a natural language like

    given ClassOne $classOne
    given ClassTwo $classtwo
    it should do something
    it should not do something
    it should do something with a really long explanation

to have an output like

    function it_should_do_something(ClassOne $classOne, ClassTwo $classtwo)
    {
    }

    function it_should_not_do_something(ClassOne $classOne, ClassTwo $classtwo)
    {
    }

    function it_should_do_something_with_a_really_long_explanation(ClassOne $classOne, ClassTwo $classtwo)
    {
    }

the "given" lines are optional and are used to specify dependencies for the <code>__construct</code> method.  
To activate the plugin select the natural language lines, bring up the Command Palette and run the "Specify - create PHPSpec test methods from selection"