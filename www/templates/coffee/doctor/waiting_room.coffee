
class WaitingRoom
  constructor: ()->
    @socket = ''
    @waiting_queue = ko.observableArray()
    @room_name = ko.observable()
    @call_in_progress = ko.observable(false)
    @joined_room = ko.observable()
    @readyToCall = ko.observable(false)

    configs =
      localVideoEl: 'localDoctorVideo'
      remoteVideosEl: 'doctorRemotesVideos'
      autoRequestMedia: true
      url: 'http://localhost:8887'

    @webrtc = new SimpleWebRTC(configs)

    webrtcReady = ()=>
      this.readyToCall(true)
      this.join_room()

    this.webrtc.on('readyToCall', webrtcReady)


  join_room: ()=>
    this.socket = io.connect('http://localhost:8886', { query: "waiting_room_number=bar" })
    this.socket.on('joined', this.joined)
    this.socket.on('patient_joined', this.patient_joined)
    this.socket.on('patient_left', this.patient_left)
    this.socket.on('call_started', this.call_started)


  joined: (data)=>
    console.log 'joined'
    console.log data

  patient_joined: (data)=>
    console.log 'patient joined the waiting room'

  patient_left: (data)=>
    console.log 'patient left the waiting room'

  call_started: (data)=>
    console.log 'call started'
    console.log data
    this.webrtc.joinRoom(data.room_token)

  start_call: ()=>
    console.log 'start a call with the next patient'
    this.call_in_progress(true)
    this.socket.emit('process_next_patient',{})

  end_call: ()=>
    console.log 'end current call'
    this.call_in_progress(false)
    this.socket.emit('disconnect_next_patient', {})
    this.webrtc.leaveRoom(this.joined_room())
    this.webrtc.stopLocalVideo()



init_waiting_room = ()->
  window.tokdoc.waiting_room = new WaitingRoom()
  ko.applyBindings(window.tokdoc.waiting_room, document.getElementById("doctor_waiting_room"));

window.tokdoc.init_waiting_room = init_waiting_room

