#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 16:48:33 2026

@author: darja
"""

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flip Card Animation</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 0;
        }

        .container {
            text-align: center;
            perspective: 1000px;
        }

        .flip-card {
            background-color: transparent;
            width: 300px;
            height: 300px;
            cursor: pointer;
            margin-bottom: 20px;
        }

        .flip-card-inner {
            position: relative;
            width: 100%;
            height: 100%;
            text-align: center;
            transition: transform 0.8s;
            transform-style: preserve-3d;
            box-shadow: 0 8px 20px rgba(0,0,0,0.3);
            border-radius: 15px;
        }

        .flip-card.flipped .flip-card-inner {
            transform: rotateY(180deg);
        }

        .flip-card-front, .flip-card-back {
            position: absolute;
            width: 100%;
            height: 100%;
            backface-visibility: hidden;
            border-radius: 15px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 20px;
            box-sizing: border-box;
        }

        .flip-card-front {
            background: white;
            color: #333;
            border: 2px solid #667eea;
        }

        .flip-card-front h2 {
            font-size: 2rem;
            margin-bottom: 10px;
            color: #667eea;
        }

        .flip-card-front p {
            font-size: 1.2rem;
            color: #666;
        }

        .flip-card-back {
            background: #667eea;
            color: white;
            transform: rotateY(180deg);
            border: 2px solid white;
        }

        .flip-card-back h2 {
            font-size: 2rem;
            margin-bottom: 10px;
        }

        .flip-card-back p {
            font-size: 1.2rem;
        }

        .instruction {
            color: white;
            font-size: 1.2rem;
            margin-top: 20px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            background: rgba(0,0,0,0.2);
            padding: 10px 20px;
            border-radius: 25px;
            display: inline-block;
        }

        /* Анимация для дополнительного эффекта */
        @keyframes pulse {
            0% {
                transform: scale(1);
            }
            50% {
                transform: scale(1.05);
            }
            100% {
                transform: scale(1);
            }
        }

        .flip-card:hover {
            animation: pulse 1s infinite;
        }

        .flip-card.flipped:hover {
            animation: none;
        }

        /* Адаптация для мобильных */
        @media (max-width: 480px) {
            .flip-card {
                width: 250px;
                height: 250px;
            }
            
            .flip-card-front h2,
            .flip-card-back h2 {
                font-size: 1.5rem;
            }
            
            .flip-card-front p,
            .flip-card-back p {
                font-size: 1rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="flip-card" id="flipCard">
            <div class="flip-card-inner">
                <!-- Передняя сторона -->
                <div class="flip-card-front">
                    <h2>Привет!</h2>
                    <p>👋</p>
                    <p>Нажми на меня</p>
                </div>
                
                <!-- Задняя сторона -->
                <div class="flip-card-back">
                    <h2>Bonjour!</h2>
                    <p>🇫🇷</p>
                    <p>Французский</p>
                </div>
            </div>
        </div>
        <div class="instruction" id="instruction">
            Нажми на карточку, чтобы перевернуть
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const flipCard = document.getElementById('flipCard');
            const instruction = document.getElementById('instruction');
            
            // Массив с парами слов для разных языков
            const wordPairs = [
                { front: 'Привет!', frontEmoji: '👋', frontDesc: 'Нажми на меня', back: 'Hello!', backEmoji: '🇬🇧', backDesc: 'Английский' },
                { front: 'Bonjour!', frontEmoji: '🇫🇷', frontDesc: 'Французский', back: 'Hola!', backEmoji: '🇪🇸', backDesc: 'Испанский' },
                { front: 'Ciao!', frontEmoji: '🇮🇹', frontDesc: 'Итальянский', back: 'Hallo!', backEmoji: '🇩🇪', backDesc: 'Немецкий' },
                { front: 'Olá!', frontEmoji: '🇵🇹', frontDesc: 'Португальский', back: 'こんにちは', backEmoji: '🇯🇵', backDesc: 'Японский' }
            ];
            
            let currentIndex = 0;
            let isFlipped = false;
            
            // Функция обновления содержимого карточки
            function updateCardContent(index, flipped) {
                const pair = wordPairs[index];
                const frontElement = document.querySelector('.flip-card-front');
                const backElement = document.querySelector('.flip-card-back');
                
                if (!flipped) {
                    frontElement.innerHTML = `
                        <h2>${pair.front}</h2>
                        <p>${pair.frontEmoji}</p>
                        <p>${pair.frontDesc}</p>
                    `;
                    backElement.innerHTML = `
                        <h2>${pair.back}</h2>
                        <p>${pair.backEmoji}</p>
                        <p>${pair.backDesc}</p>
                    `;
                } else {
                    frontElement.innerHTML = `
                        <h2>${pair.back}</h2>
                        <p>${pair.backEmoji}</p>
                        <p>${pair.backDesc}</p>
                    `;
                    backElement.innerHTML = `
                        <h2>${pair.front}</h2>
                        <p>${pair.frontEmoji}</p>
                        <p>${pair.frontDesc}</p>
                    `;
                }
            }
            
            // Обработчик клика
            flipCard.addEventListener('click', function() {
                // Переворачиваем карточку
                this.classList.toggle('flipped');
                isFlipped = this.classList.contains('flipped');
                
                // Обновляем инструкцию
                if (isFlipped) {
                    instruction.textContent = 'Сзади! Нажми ещё раз, чтобы увидеть новое слово';
                    
                    // Меняем содержимое на новую пару слов
                    setTimeout(() => {
                        currentIndex = (currentIndex + 1) % wordPairs.length;
                        updateCardContent(currentIndex, true);
                    }, 400); // Меняем в середине анимации
                } else {
                    instruction.textContent = 'Нажми на карточку, чтобы перевернуть';
                    
                    // Возвращаем исходное содержимое
                    setTimeout(() => {
                        updateCardContent(currentIndex, false);
                    }, 400);
                }
            });
            
            // Дополнительно: можно переворачивать автоматически
            // Раскомментируйте для авто-переворота каждые 3 секунды
            /*
            setInterval(() => {
                flipCard.classList.add('flipped');
                setTimeout(() => {
                    flipCard.classList.remove('flipped');
                }, 1500);
            }, 3000);
            */
        });
    </script>
</body>
</html>