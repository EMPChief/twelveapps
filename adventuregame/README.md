# Adventure Game Engine

A flexible and extensible text-based adventure game engine that uses JSON for content management. Create rich, branching narratives with items, rewards, and achievements without touching the core game code.

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## 🎮 Features

- **JSON-Driven Content**: Create adventures without coding
- **Modular Design**: Easy to extend and modify
- **Rich Game Mechanics**:
  - Branching narratives
  - Inventory system
  - Achievement tracking
  - Dynamic rewards
  - Skill checks
  - Multiple adventures

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/adventuregame.git
cd adventuregame
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the game:
```bash
python main.py
```

## 📖 Documentation

- [Architecture Overview](docs/ARCHITECTURE.md): System design and components
- [Contributing Guide](docs/CONTRIBUTING.md): How to add or modify content
- [API Documentation](docs/API.md): Technical reference

## 🎯 Creating Content

### Adventure Structure
```
adventures/
├── data/
│   ├── adventures.json    # Adventure definitions
│   ├── items.json        # Item definitions
│   ├── rewards.json      # Reward configurations
│   ├── milestones.json   # Achievement system
│   └── [adventure_name]/ # Adventure-specific content
│       └── scenes.json   # Scene definitions
```

### Quick Example

1. Create a new adventure in `adventures/data/adventures.json`:
```json
{
    "forest_quest": {
        "name": "The Enchanted Forest",
        "description": "Explore the mysterious forest...",
        "min_level": 1,
        "starting_scene": "forest_entrance",
        "completion_milestone": "forest_explorer",
        "reward_id": "forest_treasure"
    }
}
```

2. Add scenes in `adventures/data/forest_quest/scenes.json`:
```json
{
    "forest_entrance": {
        "description": "You stand at the entrance of a mystical forest...",
        "choices": {
            "1": {
                "text": "Enter the forest",
                "leads_to": "deep_forest"
            },
            "2": {
                "text": "Check your map",
                "requires_item": "forest_map"
            }
        }
    }
}
```

## 🛠️ Development

### Running Tests
```bash
python -m pytest tests/
```

### Validating Content
```bash
python adventures/validate_json.py
```

### Code Style
- Follow PEP 8
- Use descriptive names
- Add docstrings for functions
- Keep JSON files formatted

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and validation
5. Submit a pull request

See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for detailed guidelines.

## 📝 Content Guidelines

1. **Adventure Design**
   - Clear objectives
   - Multiple paths
   - Balanced rewards
   - Consistent difficulty curve

2. **Writing Style**
   - Clear descriptions
   - Engaging choices
   - Consistent tone
   - Proper grammar

3. **Game Balance**
   - Fair challenges
   - Meaningful rewards
   - Progressive difficulty
   - Multiple solutions

## 🔧 Troubleshooting

Common issues and solutions:
- Game won't start: Check Python version and dependencies
- JSON validation errors: Review file format and schema
- Missing content: Verify file paths and references
- Broken paths: Check scene connections

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Contributors and community members
- Open source libraries used
- Inspiration and references

## 📞 Contact

- GitHub Issues: For bugs and features
- Discussions: For questions and ideas
- Email: bjornmagnekristensen1999@gmail.com

---
Made with ❤️ by Bjørn-Magne
