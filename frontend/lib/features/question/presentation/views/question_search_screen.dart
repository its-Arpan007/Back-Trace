import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class QuestionSearchScreen extends StatefulWidget {
  const QuestionSearchScreen({super.key});

  @override
  State<QuestionSearchScreen> createState() => _QuestionSearchScreenState();
}

class _QuestionSearchScreenState extends State<QuestionSearchScreen> {
  final _searchController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Question Intelligence Search')),
      body: Padding(
        padding: const EdgeInsets.all(24.0),
        child: Column(
          children: [
            TextField(
              controller: _searchController,
              decoration: InputDecoration(
                hintText: 'Search by title, concept, Bloom level, or tag...',
                prefixIcon: const Icon(Icons.search_rounded, color: AppColors.accentTeal),
                filled: true,
                fillColor: AppColors.darkCard,
                border: OutlineInputBorder(borderRadius: BorderRadius.circular(12)),
              ),
              onChanged: (val) => setState(() {}),
            ),
            const SizedBox(height: 24),
            Expanded(
              child: ListView(
                children: const [
                  AppCard(
                    child: ListTile(
                      title: Text('q1_arrays_01 - Array Index Offset Calculation', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
                      subtitle: Text('Concept: DSA_ARRAYS_01 • Bloom: Apply • Type: MCQ', style: TextStyle(color: AppColors.textSecondaryDark)),
                    ),
                  ),
                  SizedBox(height: 12),
                  AppCard(
                    child: ListTile(
                      title: Text('q2_trees_01 - Binary Tree In-Order Traversal', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
                      subtitle: Text('Concept: DSA_TREES_01 • Bloom: Apply • Type: Code', style: TextStyle(color: AppColors.textSecondaryDark)),
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
