import flet as ft
import time

def main(page: ft.Page):
    page.title = "TestChat"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Chat area
    chat = ft.Column(
        spacing=10,
        scroll="auto",
        height=400,
        width=600,
        auto_scroll=True
    )

    def create_message(username, text, is_me=False):
        color = ft.colors.BLUE_400 if is_me else ft.colors.GREEN_400
        align = ft.MainAxisAlignment.END if is_me else ft.MainAxisAlignment.START
        
        return ft.Row(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(username, size=12, color=ft.colors.WHITE),
                            ft.Text(text, size=14, color=ft.colors.WHITE, selectable=True),
                            ft.Text(
                                time.strftime("%H:%M", time.localtime()),
                                size=10,
                                color=ft.colors.WHITE70,
                            ),
                        ],
                    ),
                    bgcolor=color,
                    border_radius=8,
                    padding=10,
                    width=400,
                )
            ],
            alignment=align,
        )

    def send_message(e):
        if message_field.value:
            message = create_message(username, message_field.value, True)
            chat.controls.append(message)
            chat.update()
            
            # Send message to all users
            page.pubsub.send_all({
                "username": username,
                "message": message_field.value
            })
            
            # Clear message field
            message_field.value = ""
            message_field.update()

    def on_message(message):
        # Add message to chat if not from current user
        if message["username"] != username:
            chat.controls.append(
                create_message(
                    message["username"],
                    message["message"],
                    False
                )
            )
            chat.update()

    def enter_chat(e):
        nonlocal username
        if not name_field.value:
            name_field.error_text = "Please enter your name"
            name_field.update()
            return

        username = name_field.value
        
        # Clear the page
        page.clean()
        
        # Create chat interface
        page.add(
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text(f"Chat - {username}", size=24, weight=ft.FontWeight.BOLD),
                        chat,
                        ft.Row(
                            [
                                message_field,
                                send_button
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        )
                    ],
                    spacing=20
                ),
                padding=20
            )
        )
        
        # Subscribe to receive messages
        page.pubsub.subscribe(on_message)
        
        # Send notification via pubsub
        page.pubsub.send_all({
            "username": "System",
            "message": f"{username} has joined the chat!"
        })

    # Variable to store username
    username = ""

    # Interface elements
    name_field = ft.TextField(
        width=300,
        label="Enter your name",
        autofocus=True,
        on_submit=enter_chat
    )

    message_field = ft.TextField(
        hint_text="Type your message...",
        expand=True,
        on_submit=send_message
    )

    send_button = ft.IconButton(
        icon=ft.icons.SEND,
        on_click=send_message
    )

    # Initial login screen
    page.add(
        ft.Column(
            [
                ft.Text("TestChat", size=32, weight=ft.FontWeight.BOLD),
                ft.Container(height=20),
                name_field,
                ft.Container(height=20),
                ft.ElevatedButton("Join Chat", on_click=enter_chat)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

# Start the app in web mode
ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8550) 