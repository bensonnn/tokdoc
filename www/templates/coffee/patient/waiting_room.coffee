
class WaitingRoom
  constructor: ()->
    @socket = ''
    @number_of_patients_ahead = ko.observable()
    @session_ended = ko.observable(false)
    @call_started = ko.observable(false)
    @joined_room = ko.observable()
    @ready_to_call = ko.observable(false)

    configs =
      localVideoEl: 'localPatientVideo'
      remoteVideosEl: 'patientRemotesVideos'
      autoRequestMedia: true
      url: 'http://localhost:8887'

    @webrtc = new SimpleWebRTC(configs)


    webrtcReady = ()=>
      this.ready_to_call(true)
      this.join_room()

    this.webrtc.on('readyToCall', webrtcReady)


  join_room: ()=>
    this.socket = io.connect('http://localhost:8886', { query: "waiting_room_number=bar" })
    this.socket.on('joined', this.joined)
    this.socket.on('doctor_left', this.doctor_left)
    this.socket.on('doctor_joined', this.doctor_joined)
    this.socket.on('patient_left', this.patient_left)
    this.socket.on('doctor_call_started', this.doctor_call_started)
    this.socket.on('doctor_call_ended', this.doctor_call_ended)


  joined: (data)=>
    console.log 'joined'
    console.log data
    this.number_of_patients_ahead(parseInt(data.patients_in_room))

  doctor_left: (data)=>
    console.log 'doctor left the waiting room'

  doctor_joined: (data)=>
    console.log 'doctor joined the waiting room'

  patient_left: (data)=>
    console.log 'patient left the waiting room'
    patients_ahead = this.number_of_patients_ahead() - 1
    this.number_of_patients_ahead(patients_ahead)

  doctor_call_started: (data)=>
    console.log 'doctor started a call'
    console.log data
    this.call_started(true)
    this.webrtc.joinRoom(data.room_token)

  doctor_call_ended: (data)=>
    console.log 'doctor ended a call'
    this.call_started(false)
    this.session_ended(true)
    this.webrtc.leaveRoom(this.joined_room())
    this.webrtc.stopLocalVideo()


init_waiting_room = ()->
  window.tokdoc.waiting_room = new WaitingRoom()
  ko.applyBindings(window.tokdoc.waiting_room, document.getElementById("patient_waiting_room"));


window.tokdoc.init_waiting_room = init_waiting_room