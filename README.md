# N4-Framework
 
 N4 Front-End Developpement Framework is a personnal developpement tool made to build simple websites. It uses a dynamic template + component system using Jinja. It is similar to Flask but in a static version.  

 When we talk about templates in N4, we talk about pages, each template is a page made of components or basic html css js code. A component is basically a modular element you will create, for example a buton with ajustable color, text and anything you can think of.  
 
 It also has integrated modules that are used per default such as :

 * InstantNav - Navigation module using AJAX with a custom url handling allowing to navigate trough a site without any reloads.
 * ScrollFX - Simple jQuery plugin to retract / expand / lock the navbar, it is linked to InstantNav. Documentation and standalone version available here :  https://github.com/Nepmia/N4-ScrollFX
 * TemplateRegistrator - A simple module needed to make InstantNav to work, it will analyse your template folder and register your templates names and their tiltes in a js const.

(as the project is WIP, I will list features and modules when they are created)
 
 ## Components
 
As said before,  a modular element. It can be anything you think off, butons, containers, articles, products... Anything, really. 
 
 It is similar to Angular's component system, but it's made to be extremely simple. It uses Jinja custom components system so really, it's simple, like a lot.

## InstantNav

A simple, but extremely useful system. It allow to bypass and remove the reload between your page.

Basically having an index, without content, only your head, styles and scripts. InstantNav animate a page switch, making it very intuitive and dynamic, it uses a normal url system and works with history butons.

## ScrollFX 

A very simple module that will retract and expand navbar depending on user scroll, it has multiples functions such as navlock.



N4 Framework is still in developpement features will be added with time, but for now it's just an unfinished project. 
