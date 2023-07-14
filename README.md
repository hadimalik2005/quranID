# QuranID

QuranID is a project that aims to provide an audio-based identification system for Quranic verses. Given a user audio input of a verse, the system transcribes the verse and matches it with the closest corresponding verse in the Quran.

## Features

- Audio recognition using the Levenshtein distance algorithm
- Integration with Google Cloud's speech-to-text APIs for audio transcription
- Matching audio transcriptions with the Quranic verses using textual analysis
- Python implementation

## Requirements

To run the QuranID project, you need the following dependencies:

- Python 3.x
- Levenshtein library
- Speech-to-text API credentials (e.g., Google Cloud Speech-to-Text)
