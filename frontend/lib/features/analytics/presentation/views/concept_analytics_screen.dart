import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class ConceptAnalyticsScreen extends StatelessWidget {
  const ConceptAnalyticsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Concept Performance Analytics')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              title: Text('DSA_ARRAYS_01: Memory Stride & Layout', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Avg Mastery: 75% • Failure Rate: 18% • Recovery Rate: 85%', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
