/* SPDX-License-Identifier: GPLv3-or-later */
/* Copyright (c) 2019 Project WomoLIN */
/* Author Tilo Seeck <tiloseeck@web.de> */

#include "spi.h"

SPI::SPI(SPI_HandleTypeDef *hspi) : m_phspi(hspi)
{
}

uint32_t SPI::read(std::vector<uint8_t> &data)
{
	return 0;
}

void SPI::write(const std::vector<uint8_t> &data)
{
	HAL_SPI_Transmit(m_phspi, (uint8_t *)data.data(), data.size(), 10);
}