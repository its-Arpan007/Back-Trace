import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class CurriculumSearchScreen extends StatefulWidget {
  const CurriculumSearchScreen({super.key});

  @override
  State<CurriculumSearchScreen> createState() => _CurriculumSearchScreenState();
}

class _CurriculumSearchScreenState extends State<CurriculumSearchScreen> {
  final _searchController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Curriculum & Concept Search')),
      body: Padding(
        padding: const EdgeInsets.all(24.0),
        child: Column(
          children: [
            TextField(
              controller: _searchController,
              decoration: InputDecoration(
                hintText: 'Search by concept code, title, alias, or keyword...',
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
                      title: Text('DSA_ARRAYS_01 - Array In-Memory Layout', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
                      subtitle: Text('Alias: Vector, Contiguous Memory', style: TextStyle(color: AppColors.textSecondaryDark)),
                    ),
                  ),
                  SizedBox(height: 12),
                  AppCard(
                    child: ListTile(
                      title: Text('MATH_CALC_01 - Limits & Continuity', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
                      subtitle: Text('Alias: Epsilon-Delta Definition', style: TextStyle(color: AppColors.textSecondaryDark)),
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
