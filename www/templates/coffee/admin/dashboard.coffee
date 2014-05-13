class WaitingRoom
  constructor: (room, room_data)->
    console.log 'WaitingRoom'
    console.log room
    console.log room_data
    @waiting_room_number = ko.observable(room)
    @users_waiting = ko.observable(room_data.length)


class WaitingQueueAdminDashboard
  constructor: ()->
    @socket = io.connect('http://localhost:8886')
    @waiting_rooms = ko.observableArray()
    @selected_waiting_room = ko.observable()

    this.socket.on('admin_waiting_room_created', this.waiting_room_created)
    this.socket.on('admin_user_joined_room', this.user_joined_room)
    this.socket.on('admin_user_left_room', this.user_left_room)
    this.socket.on('admin_init', this.admin_init)
    this.socket.emit('admin_init')


  admin_init: (data)=>
    console.log data.waitingQueues
    this.waiting_rooms([])

    for room in Object.keys(data.waitingQueues)
      console.log room
      room_data = data.waitingQueues[room]
      waiting_room = new WaitingRoom(room, room_data)
      this.waiting_rooms.push(waiting_room)
      this.selected_waiting_room(waiting_room)

  waiting_room_created: (data)=>
    console.log 'created waiting room'
    for room in Object.keys(data.waitingQueues)
      console.log room
      room_data = data.waitingQueues[room]
      waiting_room = new WaitingRoom(room, room_data)
      this.waiting_rooms.push(waiting_room)

  user_joined_room: (data)=>
    console.log 'user joined room'
    console.log data

  user_left_room: (data)=>
    console.log 'user left the room'



window.tokdoc.dashboard = new WaitingQueueAdminDashboard()

ko.applyBindings(window.tokdoc.dashboard, document.getElementById("dashboard"));