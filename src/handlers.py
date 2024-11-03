from telegram import Update
from telegram.ext import CallbackContext
from datetime import datetime
from config import ADMIN_IDS, LUNCH_BREAK_LIMIT, SMOKE_BREAK_LIMIT, RESTROOM_BREAK_LIMIT
from src.models import UserManager

user_manager = UserManager()

def start_command(update: Update, context: CallbackContext) -> None:
    """Send welcome message when /start is issued."""
    update.message.reply_text(
        'Welcome to Work Shift Manager Bot!\n\n'
        'Commands:\n'
        '/start_shift - Start your work shift\n'
        '/end_shift - End your work shift\n'
        '/break <type> - Start a break (lunch/smoke/restroom)\n'
        '/end_break - End your current break\n'
        '/status - Check your current status'
    )

def start_shift(update: Update, context: CallbackContext) -> None:
    """Start a new work shift."""
    user_id = update.effective_user.id
    if user_manager.start_shift(user_id):
        update.message.reply_text(
            f"Shift started at {datetime.now().strftime('%H:%M:%S')}"
        )
    else:
        update.message.reply_text("You already have an active shift!")

def end_shift(update: Update, context: CallbackContext) -> None:
    """End the current work shift."""
    user_id = update.effective_user.id
    hours = user_manager.end_shift(user_id)
    
    if hours is not None:
        update.message.reply_text(
            f"Shift ended. Total hours worked: {hours:.2f}"
        )
    else:
        update.message.reply_text("You don't have an active shift!")

def start_break(update: Update, context: CallbackContext) -> None:
    """Start a break with specified type."""
    if not context.args:
        update.message.reply_text("Please specify break type: lunch/smoke/restroom")
        return
        
    break_type = context.args[0].lower()
    user_id = update.effective_user.id
    
    if break_type not in ['lunch', 'smoke', 'restroom']:
        update.message.reply_text("Invalid break type. Use: lunch/smoke/restroom")
        return
        
    if user_id in user_manager.active_breaks:
        update.message.reply_text("You already have an active break!")
        return
        
    user_manager.active_breaks[user_id] = Break(break_type, user_id)
    update.message.reply_text(f"{break_type.title()} break started!")

def end_break(update: Update, context: CallbackContext) -> None:
    """End the current break."""
    user_id = update.effective_user.id
    
    if user_id not in user_manager.active_breaks:
        update.message.reply_text("You don't have an active break!")
        return
        
    break_obj = user_manager.active_breaks[user_id]
    duration = break_obj.end()
    del user_manager.active_breaks[user_id]
    
    limit = {
        'lunch': LUNCH_BREAK_LIMIT,
        'smoke': SMOKE_BREAK_LIMIT,
        'restroom': RESTROOM_BREAK_LIMIT
    }[break_obj.type]
    
    if duration > limit:
        message = f"Break ended. WARNING: Break duration ({duration:.1f}min) exceeded limit ({limit}min)!"
        # Notify admins
        for admin_id in ADMIN_IDS:
            context.bot.send_message(
                chat_id=admin_id,
                text=f"User {user_id} exceeded {break_obj.type} break limit: {duration:.1f}min"
            )
    else:
        message = f"Break ended. Duration: {duration:.1f}min"
    
    update.message.reply_text(message)