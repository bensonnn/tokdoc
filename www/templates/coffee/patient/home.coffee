window.tokdoc.navbar.show_user_login(false)


class Doctor

  constructor: (email)->
    @email = ko.observable(email)

  view_profile_click: ()->
    console.log 'clicked ' + this.email()
    window.location = '/doctor/' + this.email()



class Home

  constructor: ()->
    @doctor_contacts = ko.observableArray([])

    load_doctors = (data)=>
      for doctor_email in data.doctor_contacts
        doctor = new Doctor(doctor_email)
        this.doctor_contacts.push(doctor)

      console.log data
    $.get('/api/get_doctors/', load_doctors)


window.tokdoc.home = new Home()
ko.applyBindings(window.tokdoc.home, document.getElementById("patient_home"));


