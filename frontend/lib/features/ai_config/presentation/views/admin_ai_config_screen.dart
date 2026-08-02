import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class AdminAiConfigScreen extends StatelessWidget {
  const AdminAiConfigScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('AI Prompts & Feature Flags Configuration')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              leading: Icon(Icons.psychology_rounded, color: AppColors.accentOrange),
              title: Text('Model Version: gemini-1.5-pro', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Adaptive Practice: ENABLED • AI Explanation: ENABLED • Safety Rules: 12 Active', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
