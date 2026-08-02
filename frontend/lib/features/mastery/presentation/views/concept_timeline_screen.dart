import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class ConceptTimelineScreen extends StatelessWidget {
  const ConceptTimelineScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final timelinePoints = [
      {"label": "Day 1", "score": "34%", "desc": "Initial Diagnostic Attempt"},
      {"label": "Day 4", "score": "51%", "desc": "Practice Set 1 Completed"},
      {"label": "Day 9", "score": "69%", "desc": "Prerequisite Review Session"},
      {"label": "Day 14", "score": "88%", "desc": "Latest Assessment Update (Mastered)"},
    ];

    return Scaffold(
      appBar: AppBar(title: const Text('Concept Mastery Timeline')),
      body: ListView.builder(
        padding: const EdgeInsets.all(24),
        itemCount: timelinePoints.length,
        itemBuilder: (context, idx) {
          final pt = timelinePoints[idx];
          return Column(
            children: [
              AppCard(
                child: ListTile(
                  leading: CircleAvatar(
                    backgroundColor: AppColors.accentTeal,
                    child: Text(pt["label"]!.replaceFirst("Day ", "D"), style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 12)),
                  ),
                  title: Text('${pt["label"]} — ${pt["score"]} Mastery', style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
                  subtitle: Text(pt["desc"]!, style: const TextStyle(color: AppColors.textSecondaryDark)),
                ),
              ),
              if (idx < timelinePoints.length - 1)
                const Padding(
                  padding: EdgeInsets.symmetric(vertical: 8.0),
                  child: Icon(Icons.arrow_downward_rounded, color: AppColors.accentTeal),
                ),
            ],
          );
        },
      ),
    );
  }
}
