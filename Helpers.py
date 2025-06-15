import re

def remove_country_flags(pair):
    """
    Удаляет эмодзи флагов стран из строки валютной пары.
    """
    emoji_pattern = re.compile("[\U0001F1E6-\U0001F1FF\s]+")  # Соответствует эмодзи флагов стран и пробелам
    return emoji_pattern.sub("", pair).strip()

def format_indicators(indicators):
    """
    Форматирует объект индикаторов в удобочитаемую строку с эмодзи и табуляцией.
    """
    lines = []

    # Основной заголовок
    lines.append("📊 **Анализ Индикаторов**\n")
    lines.append("━━━━━━━━━━━━━━━━━━━━━━━")

    # Добавление отдельных индикаторов
    if 'RSI' in indicators:
        lines.append(f"📈 **RSI**: {indicators['RSI']:.2f} 🎯")

    if 'EMA' in indicators:
        lines.append(f"📊 **EMA**: {indicators['EMA']:.5f}")

    if 'MACD' in indicators:
        lines.append("📊 **MACD**:")
        lines.append(f"   ├─ MACD: {indicators['MACD']['MACD']:.5f}")
        lines.append(f"   └─ Сигнал: {indicators['MACD']['Signal']:.5f}")

    if 'Bollinger Bands' in indicators:
        bb = indicators['Bollinger Bands']
        lines.append("📊 **Полосы Боллинджера**:")
        lines.append(f"   ├─ Верхняя Полоса: {bb['Upper Band']:.5f}")
        lines.append(f"   ├─ Нижняя Полоса: {bb['Lower Band']:.5f}")
        lines.append(f"   └─ Средняя Полоса: {bb['Middle Band']:.5f}")

    if 'Stochastic Oscillator' in indicators:
        so = indicators['Stochastic Oscillator']
        lines.append("📊 **Стохастический Осциллятор**:")
        lines.append(f"   ├─ %K: {so['%K']:.2f}")
        lines.append(f"   └─ %D: {so['%D']:.2f}")

    if 'Support and Resistance' in indicators:
        sr = indicators['Support and Resistance']
        lines.append("📊 **Уровни Поддержки и Сопротивления**:")
        lines.append(f"   ├─ Поддержка: {sr['Support']:.5f}")
        lines.append(f"   └─ Сопротивление: {sr['Resistance']:.5f}")

    if 'Keltner Channels' in indicators:
        kc = indicators['Keltner Channels']
        lines.append("📊 **Каналы Келтнера**:")
        lines.append(f"   ├─ Верхняя Полоса: {kc['Upper Band']:.5f}")
        lines.append(f"   ├─ Нижняя Полоса: {kc['Lower Band']:.5f}")
        lines.append(f"   └─ Средняя Линия: {kc['Middle Line']:.5f}")

    if 'Parabolic SAR' in indicators:
        lines.append(f"📊 **Параболический SAR**: {indicators['Parabolic SAR']:.5f}")

    if 'Fibonacci Retracement' in indicators:
        fr = indicators['Fibonacci Retracement']
        lines.append("📊 **Уровни Фибоначчи**:")
        for level, value in fr.items():
            lines.append(f"   └─ {level}: {value:.5f}")

    # Финальный разделитель
    lines.append("━━━━━━━━━━━━━━━━━━━━━━━")

    # Объединение строк в форматированную строку
    return "\n".join(lines)

def format_summary(summary):
    """
    Форматирует объект сводки в удобочитаемую строку с эмодзи и табуляцией.
    """
    lines = []

    # Основной заголовок
    lines.append("📊 **Сводка**\n")
    lines.append("━━━━━━━━━━━━━━━━━━━━━━━")

    # Добавление деталей сводки
    if 'Open' in summary:
        lines.append(f"📈 **Открытие**: {summary['Open']:.5f}")
    if 'High' in summary:
        lines.append(f"📈 **Максимум**: {summary['High']:.5f}")
    if 'Low' in summary:
        lines.append(f"📉 **Минимум**: {summary['Low']:.5f}")
    if 'Close' in summary:
        lines.append(f"📉 **Закрытие**: {summary['Close']:.5f}")
    if 'Volume' in summary:
        lines.append(f"📊 **Объем**: {summary['Volume']}")
    if 'Start Time' in summary:
        lines.append(f"⏲️ **Начальное Время**: {summary['Start Time']}")
    if 'End Time' in summary:
        lines.append(f"⏲️ **Конечное Время**: {summary['End Time']}")
    if 'Top Value Time' in summary:
        lines.append(f"⭐ **Время Максимального Значения**: {summary['Top Value Time']}")
    if 'Bottom Value Time' in summary:
        lines.append(f"⭐ **Время Минимального Значения**: {summary['Bottom Value Time']}")

    # Финальный разделитель
    lines.append("━━━━━━━━━━━━━━━━━━━━━━━")

    # Объединение строк в форматированную строку
    return "\n".join(lines)

def print_indicators(results):
    """
    Выводит индикаторы и сводку.
    """
    if not results:
        print("Нет результатов для отображения.")
        return

    print("\n📊 **Сводка**:")
    for key, value in results["Summary"].items():
        print(f"{key}: {value}")

    print("\n📊 **Индикаторы**:")
    for indicator, value in results["Indicators"].items():
        print(f"{indicator}: {value}")

# import re

# def remove_country_flags(pair):
#     """
#     Removes country flag emojis from the currency pair string.
#     """
#     emoji_pattern = re.compile("[\U0001F1E6-\U0001F1FF\s]+")  # Matches country flag emojis and spaces
#     return emoji_pattern.sub("", pair).strip()

# def format_indicators(indicators):
#     """
#     Formats the indicators object into a user-friendly string with emojis and tabbing.
#     """
#     lines = []

#     # Add main heading
#     lines.append("📊 **Indicator Analysis**\n")
#     lines.append("━━━━━━━━━━━━━━━━━━━━━━━")

#     # Add individual indicators with formatting
#     if 'RSI' in indicators:
#         lines.append(f"📈 **RSI**: {indicators['RSI']:.2f} 🎯")

#     if 'EMA' in indicators:
#         lines.append(f"📊 **EMA**: {indicators['EMA']:.5f}")

#     if 'MACD' in indicators:
#         lines.append("📊 **MACD**:")
#         lines.append(f"   ├─ MACD: {indicators['MACD']['MACD']:.5f}")
#         lines.append(f"   └─ Signal: {indicators['MACD']['Signal']:.5f}")

#     if 'Bollinger Bands' in indicators:
#         bb = indicators['Bollinger Bands']
#         lines.append("📊 **Bollinger Bands**:")
#         lines.append(f"   ├─ Upper Band: {bb['Upper Band']:.5f}")
#         lines.append(f"   ├─ Lower Band: {bb['Lower Band']:.5f}")
#         lines.append(f"   └─ Middle Band: {bb['Middle Band']:.5f}")

#     if 'Stochastic Oscillator' in indicators:
#         so = indicators['Stochastic Oscillator']
#         lines.append("📊 **Stochastic Oscillator**:")
#         lines.append(f"   ├─ %K: {so['%K']:.2f}")
#         lines.append(f"   └─ %D: {so['%D']:.2f}")

#     if 'Support and Resistance' in indicators:
#         sr = indicators['Support and Resistance']
#         lines.append("📊 **Support and Resistance**:")
#         lines.append(f"   ├─ Support: {sr['Support']:.5f}")
#         lines.append(f"   └─ Resistance: {sr['Resistance']:.5f}")

#     if 'Keltner Channels' in indicators:
#         kc = indicators['Keltner Channels']
#         lines.append("📊 **Keltner Channels**:")
#         lines.append(f"   ├─ Upper Band: {kc['Upper Band']:.5f}")
#         lines.append(f"   ├─ Lower Band: {kc['Lower Band']:.5f}")
#         lines.append(f"   └─ Middle Line: {kc['Middle Line']:.5f}")

#     if 'Parabolic SAR' in indicators:
#         lines.append(f"📊 **Parabolic SAR**: {indicators['Parabolic SAR']:.5f}")

#     if 'Fibonacci Retracement' in indicators:
#         fr = indicators['Fibonacci Retracement']
#         lines.append("📊 **Fibonacci Retracement Levels**:")
#         for level, value in fr.items():
#             lines.append(f"   └─ {level}: {value:.5f}")

#     # Final separator
#     lines.append("━━━━━━━━━━━━━━━━━━━━━━━")

#     # Join lines into a formatted string
#     return "\n".join(lines)

# def format_summary(summary):
#     """
#     Formats the summary object into a user-friendly string with proper tabbing and emojis.
#     """
#     lines = []

#     # Add main heading
#     lines.append("📊 **Summary**\n")
#     lines.append("━━━━━━━━━━━━━━━━━━━━━━━")

#     # Add summary details
#     if 'Open' in summary:
#         lines.append(f"📈 **Open**: {summary['Open']:.5f}")
#     if 'High' in summary:
#         lines.append(f"📈 **High**: {summary['High']:.5f}")
#     if 'Low' in summary:
#         lines.append(f"📉 **Low**: {summary['Low']:.5f}")
#     if 'Close' in summary:
#         lines.append(f"📉 **Close**: {summary['Close']:.5f}")
#     if 'Volume' in summary:
#         lines.append(f"📊 **Volume**: {summary['Volume']}")
#     if 'Start Time' in summary:
#         lines.append(f"⏲️ **Start Time**: {summary['Start Time']}")
#     if 'End Time' in summary:
#         lines.append(f"⏲️ **End Time**: {summary['End Time']}")
#     if 'Top Value Time' in summary:
#         lines.append(f"⭐ **Top Value Time**: {summary['Top Value Time']}")
#     if 'Bottom Value Time' in summary:
#         lines.append(f"⭐ **Bottom Value Time**: {summary['Bottom Value Time']}")

#     # Final separator
#     lines.append("━━━━━━━━━━━━━━━━━━━━━━━")

#     # Join lines into a formatted string
#     return "\n".join(lines)


# def print_indicators(results):
#         if not results:
#             print("No results to display.")
#             return

#         print("\nSummary:")
#         for key, value in results["Summary"].items():
#             print(f"{key}: {value}")

#         print("\nIndicators:")
#         for indicator, value in results["Indicators"].items():
#             print(f"{indicator}: {value}")