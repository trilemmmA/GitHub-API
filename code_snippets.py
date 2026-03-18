{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNE7/0VbtEWiQ0a7y/7UXcb"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "dpX1GDqgSHRS"
      },
      "outputs": [],
      "source": [
        "from openai import OpenAI\n",
        "from dotenv import load_dotenv\n",
        "import os\n",
        "import sys\n",
        "import logging\n",
        "\n",
        "load_dotenv()\n",
        "\n",
        "apikey = os.getenv(\"BOTKEY\", \"\")\n",
        "if not apikey:\n",
        "    logging.error(f\"There is no API key, try again later...\")\n",
        "    sys.exit(1)\n",
        "\n",
        "system_prompt = \"\"\"Тебе дается текст, исправь текст на более грамматически правильный и без воды, укажи на ошибки\"\"\"\n",
        "\n",
        "llm = OpenAI(api_key=apikey)\n",
        "\n",
        "def get_answer(user_query: str):\n",
        "    try:\n",
        "        resp = llm.chat.completions.create(\n",
        "            model=\"gpt-4o\", messages=[\n",
        "                {\"role\": \"system\", \"content\": f\"{system_prompt}\"},\n",
        "                {\"role\": \"user\", \"content\": user_query}\n",
        "        ]\n",
        "    )\n",
        "        return resp.choices[0].message.content\n",
        "\n",
        "    except Exception as e:\n",
        "        logging.error(f\"LLM Error: {e}\")\n",
        "        return None"
      ]
    }
  ]
}