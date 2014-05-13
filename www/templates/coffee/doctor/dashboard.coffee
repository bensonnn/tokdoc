window.tokdoc.navbar.show_user_login(false)


class Patient
  constructor: ()->
    @full_name = ko.observable()
    @problem = ko.observable()
    @age = ko.observable()
    @webrtc = ko.observable()

  end_and_answer: ()=>
    console.log 'end and answer'

  end_call: ()=>
    console.log 'end call'
    new_patient = window.tokdoc.dashboard.answer_next_patient()


class Dashboard
  constructor: ()->
    patient_1 = new Patient()
    patient_1.full_name("Vijay Selvaraj")
    patient_1.problem("cough")
    patient_1.age("age 32")
    patient_2 = new Patient()
    patient_2.full_name("John Brown")
    patient_2.problem("problem 2")
    patient_2.age("age 1")
    patient_3 = new Patient()
    patient_3.full_name("Kelly Simons")
    patient_3.problem("stomach issue")
    patient_3.age("2")


    @waiting_patients = ko.observableArray([patient_2, patient_3])
    @speaking_with_patient = ko.observable(patient_1)

    @socket = io.connect('http://localhost:8887/')

    this.init_video()




  init_video: ()->

    configs =
      localVideoEl: 'localVideo'
      remoteVideosEl: 'remoteVideo'
      autoRequestMedia: true,
      url: 'http://localhost:8887'

    this.webrtc = new SimpleWebRTC(configs)

    joinRoom = (room)=>
      console.log 'joining room ' + room
      this.webrtc.joinRoom(room)

    room_created = (room)=>
      console.log 'room created!'
      console.log room

      joinRoom(room)

    this.socket.on('room_created', room_created)
    this.socket.emit('create_room',{})


    this.webrtc.on('readyToCall', joinRoom)





#    handleVideo = (stream) ->
#      remoteVideo.src = window.URL.createObjectURL(stream)
#      localVideo.src = window.URL.createObjectURL(stream)
#      return
#    videoError = (e) ->
 #   remoteVideo = document.querySelector("#remoteVideo")
 #   localVideo = document.querySelector("#localVideo")
 #   navigator.getUserMedia = navigator.getUserMedia or navigator.webkitGetUserMedia or navigator.mozGetUserMedia or navigator.msGetUserMedia or navigator.oGetUserMedia
 #   if navigator.getUserMedia
 #     navigator.getUserMedia
 #       video: true
 #     , handleVideo, videoError


  new_waiting_patient: (patient)->
    this.waiting_patients.push(patient)

  answer_next_patient: ()->
    patients = window.tokdoc.dashboard.waiting_patients.peek()
    if patients
      patient = patients[0]
      window.tokdoc.dashboard.waiting_patients.remove(patient)
      window.tokdoc.dashboard.speaking_with_patient(patient)



window.tokdoc.dashboard = new Dashboard()

ko.applyBindings(window.tokdoc.dashboard, document.getElementById("dashboard"));









