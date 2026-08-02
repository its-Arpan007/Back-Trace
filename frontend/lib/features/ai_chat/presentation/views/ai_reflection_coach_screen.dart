import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class AIReflectionCoachScreen extends StatelessWidget {
  const AIReflectionCoachScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('AI Self-Reflection Guidance')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              leading: Icon(Icons.help_outline_rounded, color: AppColors.accentTeal),
              title: Text('Reflect on Array Offset Arithmetic', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Prompt: What assumption did you make when calculating the base memory offset?', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
