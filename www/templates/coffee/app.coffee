console.log 'app init'

window.tokdoc = {}

class NavigationBar
  constructor: ()->
    @logo = ko.observable(true)
    @show_user_login = ko.observable(true)

window.tokdoc.navbar = new NavigationBar()

