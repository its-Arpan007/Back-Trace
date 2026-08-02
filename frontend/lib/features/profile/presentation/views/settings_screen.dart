import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';

class SettingsScreen extends StatelessWidget {
  const SettingsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Platform Settings')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: [
          ListTile(
            leading: const Icon(Icons.palette_outlined, color: AppColors.accentTeal),
            title: const Text('Theme Preference', style: TextStyle(color: Colors.white)),
            subtitle: const Text('Dark Slate (Default)', style: TextStyle(color: AppColors.textSecondaryDark)),
          ),
          const Divider(color: AppColors.darkBorder),
          ListTile(
            leading: const Icon(Icons.language_outlined, color: AppColors.accentTeal),
            title: const Text('Language', style: TextStyle(color: Colors.white)),
            subtitle: const Text('English (US)', style: TextStyle(color: AppColors.textSecondaryDark)),
          ),
        ],
      ),
    );
  }
}
