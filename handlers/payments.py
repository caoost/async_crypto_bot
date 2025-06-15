from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import logging

router = Router()
logger = logging.getLogger(__name__)

@router.message(F.text == "Pay USDT")
async def process_crypto_payment(message: Message, state: FSMContext):
    """Handles crypto payment generation and verification."""
    logger.info(f"User {message.from_user.id} requested payment details.")
    # Stub for TRON API / CryptoPay integration
    wallet_address = "TXYZ...mock_address...1234"
    await message.answer(
        f"Please send exact amount to TRC-20 wallet:\n`{wallet_address}`\n\n"
        "Click 'Verify' after transaction is completed.",
        parse_mode="Markdown"
    )
    await state.set_state("waiting_for_tx_hash")