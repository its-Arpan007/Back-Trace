import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class ConceptExplainerScreen extends StatelessWidget {
  const ConceptExplainerScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('AI Concept Explainer & Analogies')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              leading: Icon(Icons.lightbulb_rounded, color: AppColors.accentTeal, size: 36),
              title: Text('Memory Stride Analogy', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Think of memory addresses like postal mailboxes arranged in a linear row. Each box holds 4 bytes.', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
