/* SPDX-License-Identifier: GPLv3-or-later */
/* Copyright (c) 2019 Project WomoLIN */
/* Author Tilo Seeck <tiloseeck@web.de> */
#include "uart.h"

Uart::Uart(UART_HandleTypeDef *huart, CircularBuffer<uint8_t> *buffer) : m_phuart(huart), m_pbuffer(buffer), m_lastsendsize(0)
{
	InterruptHandler::registerCallback(IRQ_UART1, Uart::irquarthandler, this);
}

uint32_t Uart::read(std::string &data)
{
	if(!m_pbuffer->empty()) {
		size_t size = m_pbuffer->size();
		for(size_t i = 0; i < size; i++) {
			uint8_t byte = m_pbuffer->get();
			// Filter last send bytes.
			if(m_lastsendsize > 0) {
				m_lastsendsize--;
				continue;
			}
			data += byte;
		}
	}

	return data.length();
}

void Uart::write(const std::string &data)
{
	HAL_UART_Transmit(m_phuart, (uint8_t *) data.c_str(), data.length(), 100);
	m_lastsendsize = data.length();
}

void Uart::irqhandler()
{
	uint8_t byte = m_phuart->Instance->RDR;
	m_pbuffer->put(byte);
	HAL_UART_IRQHandler(m_phuart);
}

void Uart::irquarthandler(void *param)
{
	Uart *puart = (Uart *)param;
	puart->irqhandler();
}

