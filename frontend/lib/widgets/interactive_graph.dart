import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';

class GraphNodeData {
  final String id;
  final String label;
  final String domain;
  final Offset position;
  final bool isTarget;
  final bool isHighlighted;

  GraphNodeData({
    required this.id,
    required this.label,
    required this.domain,
    required this.position,
    this.isTarget = false,
    this.isHighlighted = false,
  });
}

class GraphEdgeData {
  final String sourceId;
  final String targetId;
  final String type;

  GraphEdgeData({required this.sourceId, required this.targetId, this.type = 'Prerequisite'});
}

class InteractiveKnowledgeGraphWidget extends StatefulWidget {
  final List<GraphNodeData> nodes;
  final List<GraphEdgeData> edges;
  final Function(GraphNodeData)? onNodeSelected;

  const InteractiveKnowledgeGraphWidget({
    super.key,
    required this.nodes,
    required this.edges,
    this.onNodeSelected,
  });

  @override
  State<InteractiveKnowledgeGraphWidget> createState() => _InteractiveKnowledgeGraphWidgetState();
}

class _InteractiveKnowledgeGraphWidgetState extends State<InteractiveKnowledgeGraphWidget> {
  String? _selectedNodeId;

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        color: AppColors.darkBackground,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: AppColors.darkBorder),
      ),
      child: ClipRRect(
        borderRadius: BorderRadius.circular(16),
        child: InteractiveViewer(
          boundaryMargin: const EdgeInsets.all(100),
          minScale: 0.5,
          maxScale: 2.5,
          child: SizedBox(
            width: 800,
            height: 600,
            child: Stack(
              children: [
                // Custom Painter for Directional Edges
                CustomPaint(
                  size: const Size(800, 600),
                  painter: _GraphEdgePainter(
                    nodes: widget.nodes,
                    edges: widget.edges,
                    selectedNodeId: _selectedNodeId,
                  ),
                ),

                // Interactive Nodes
                ...widget.nodes.map((node) {
                  final isSelected = node.id == _selectedNodeId;
                  final color = node.isTarget
                      ? AppColors.accentCyan
                      : node.isHighlighted
                          ? AppColors.accentTeal
                          : AppColors.accentIndigo;

                  return Positioned(
                    left: node.position.dx - 60,
                    top: node.position.dy - 30,
                    child: GestureDetector(
                      onTap: () {
                        setState(() => _selectedNodeId = node.id);
                        if (widget.onNodeSelected != null) {
                          widget.onNodeSelected!(node);
                        }
                      },
                      child: AnimatedContainer(
                        duration: const Duration(milliseconds: 200),
                        width: 120,
                        padding: const EdgeInsets.all(8),
                        decoration: BoxDecoration(
                          color: AppColors.darkCard,
                          borderRadius: BorderRadius.circular(12),
                          border: Border.all(
                            color: isSelected ? Colors.white : color,
                            width: isSelected ? 2.5 : 1.5,
                          ),
                          boxShadow: [
                            BoxShadow(
                              color: color.withOpacity(0.3),
                              blurRadius: isSelected ? 12 : 6,
                            ),
                          ],
                        ),
                        child: Column(
                          mainAxisSize: MainAxisSize.min,
                          children: [
                            Text(
                              node.label,
                              textAlign: TextAlign.center,
                              maxLines: 2,
                              overflow: TextOverflow.ellipsis,
                              style: TextStyle(
                                color: Colors.white,
                                fontSize: 11,
                                fontWeight: isSelected ? FontWeight.bold : FontWeight.w600,
                              ),
                            ),
                            const SizedBox(height: 4),
                            Container(
                              padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                              decoration: BoxDecoration(
                                color: color.withOpacity(0.2),
                                borderRadius: BorderRadius.circular(8),
                              ),
                              child: Text(
                                node.id,
                                style: TextStyle(color: color, fontSize: 9, fontWeight: FontWeight.bold),
                              ),
                            ),
                          ],
                        ),
                      ),
                    ),
                  );
                }).toList(),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

class _GraphEdgePainter extends CustomPainter {
  final List<GraphNodeData> nodes;
  final List<GraphEdgeData> edges;
  final String? selectedNodeId;

  _GraphEdgePainter({
    required this.nodes,
    required this.edges,
    this.selectedNodeId,
  });

  @override
  void paint(Canvas canvas, Size size) {
    final Map<String, Offset> posMap = {for (var n in nodes) n.id: n.position};

    for (var edge in edges) {
      final src = posMap[edge.sourceId];
      final tgt = posMap[edge.targetId];

      if (src != null && tgt != null) {
        final isConnected = selectedNodeId == edge.sourceId || selectedNodeId == edge.targetId;
        final paint = Paint()
          ..color = isConnected ? AppColors.accentCyan : AppColors.darkBorder
          ..strokeWidth = isConnected ? 2.5 : 1.5
          ..style = PaintingStyle.stroke;

        canvas.drawLine(src, tgt, paint);
      }
    }
  }

  @override
  bool shouldRepaint(covariant _GraphEdgePainter oldDelegate) => true;
}
